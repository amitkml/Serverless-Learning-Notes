# Understanding state and application workflows with AWS Step Functions

## InputPath, Parameters and ResultSelector

The `InputPath`, `Parameters` and `ResultSelector` fields provide a way to manipulate JSON as it moves through your workflow. The `Parameters` field enables you to pass a collection of key-value pairs, where the values are either static values that you define in your state machine definition, or that are selected from the input using a path. The `ResultSelector` field provides a way to manipulate the state’s result before `ResultPath` is applied.

AWS Step Functions applies the `InputPath` field first, and then the `Parameters` field. You can first filter your raw input to a selection you want using `InputPath`, and then apply `Parameters` to manipulate that input further, or add new values. You can then use the `ResultSelector` field to manipulate the state's output before `ResultPath` is applied.

Step function follows following order of execution. ![im](https://github.com/amitkml/Serverless-Learning-Notes/blob/main/images/step_function_order_ops.JPG?raw=true)

### InputPath

Use `InputPath` to select a portion of the state input.

Ex:  input to your state includes the following.

```json
{
  "comment": "Example for InputPath.",
  "dataset1": {
    "val1": 1
  },
  "dataset2": {
    "val1": "a",
    "val2": "b",
    "val3": "c"
  }
}
```

We apply the `InputPath`.

```json
"InputPath": "$.dataset2",
```

With the previous `InputPath`, the following is the JSON that is passed as the input to state task.

```json
{
  "val1": "a",
  "val2": "b",
  "val3": "c"
}
```

Lets understand more from following example.![im](https://github.com/amitkml/Serverless-Learning-Notes/blob/main/images/InputPath_Translation.JPG?raw=true)

Here,  our InputPath is set to $.InvokingEvent and this means from input event, the InputPath will filter InvokingEvent element and pass on to state task.

### Parameters

We can use parameter in following different ways.

#### Key-value pairs

Use the `Parameters` field to create a collection of key-value pairs that are passed as input. The values of each can either be static values that you include in your state machine definition, or selected from either the input or the context object with a path.

It is important to note that, *key-value pairs where the value is selected using a path, the key name must end in `.$`.*

Ex: Input to state machine

```json
{
  "comment": "Example for Parameters.",
  "product": {
    "details": {
       "color": "blue",
       "size": "small",
       "material": "cotton"
    },
    "availability": "in stock"
  }
}
```

For a subset selection, specify these parameters in your state machine definition.

- here size and exists input are being taken from InputPath and hence we have $ added at end of the variable.
- StaticValue is not being populated from any InputPath and hence no $ sign added at last.

```json
"Parameters": {
        "comment": "Selecting input what I need.",
        "MyDetails": {
          "size.$": "$.product.details.size",
          "exists.$": "$.product.availability",
          "StaticValue": "foo"
        }
      },
```

Given the previous input and the `Parameters` field, this is the JSON that is passed to the state task.

```json
{
  "comment": "Selecting input what I need.",
  "MyDetails": {
      "size": "small",
      "exists": "in stock",
      "StaticValue": "foo"
  }
},
```

#### Connected resources

The `Parameters` field can also pass information to connected resources. For example, if your task state is orchestrating an AWS Batch job, you can pass the relevant API parameters directly to the API actions of that service.  <<TBD>>

### ResultSelector

Use the `ResultSelector` field to manipulate a state's result before `ResultPath` is applied. The `ResultSelector` field lets you create a collection of key value pairs, where the values are static or selected from the state's result. The output of `ResultSelector` replaces the state's result and is passed to `ResultPat`

`ResultSelector` is an optional field in the following states:

- Map
- Parallel
- Task  