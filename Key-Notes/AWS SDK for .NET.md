# AWS SDK for .NET

Please always refer to [What is the AWS SDK for .NET](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/welcome.html) for guide. ![Image](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/images/overview.png)

All the packages can be found from https://www.nuget.org/packages?q=id%3AAWSSDK%20owner%3Aawsdotnet

## Building a AWS Comprehend C# Console application

### Create the project

Go into command prompt under which you can create a .NET project and then 

```
dotnet new console --name Comprehend
```

Go to the newly created `Comprehend folder and run the following command.\

```
dotnet add package AWSSDK.S3
dotnet add package AWSSDK.Core
dotnet add package AWSSDK.Comprehend
```

Following are **key output log informations** that we need to watch during adding package and they are essential for my project…

- “Installing AWSSDK.Comprehend 3.5.2.21.”
- “Package 'AWSSDK.Comprehend' is compatible with all the specified frameworks in project”
- “Package 'AWSSDK.Comprehend' is compatible with all the specified frameworks in project in Comprehend.csproj”
- “PackageReference for package 'AWSSDK.Comprehend' version '3.5.2.21' added to file 'Comprehend.csproj'”

```
C:\Amit Project\Programming-POC\C#\Practise\Fundamentals\aws-stuff\comprehend\src\Comprehend>dotnet add package AWSSDK.Comprehend
  Determining projects to restore...
  Writing C:\Users\akayal\AppData\Local\Temp\1\tmpE7AE.tmp
info : Adding PackageReference for package 'AWSSDK.Comprehend' into project 'C:\Amit Project\Programming-POC\C#\Practise\Fundamentals\aws-stuff\comprehend\src\Comprehend\Comprehend.csproj'.
info : Restoring packages for C:\Amit Project\Programming-POC\C#\Practise\Fundamentals\aws-stuff\comprehend\src\Comprehend\Comprehend.csproj...
info :   GET https://api.nuget.org/v3-flatcontainer/awssdk.comprehend/index.json
info :   OK https://api.nuget.org/v3-flatcontainer/awssdk.comprehend/index.json 1228ms
info :   GET https://api.nuget.org/v3-flatcontainer/awssdk.comprehend/3.5.2.21/awssdk.comprehend.3.5.2.21.nupkg
info :   OK https://api.nuget.org/v3-flatcontainer/awssdk.comprehend/3.5.2.21/awssdk.comprehend.3.5.2.21.nupkg 1117ms
info : Installing AWSSDK.Comprehend 3.5.2.21.
info : Package 'AWSSDK.Comprehend' is compatible with all the specified frameworks in project 'C:\Amit Project\Programming-POC\C#\Practise\Fundamentals\aws-stuff\comprehend\src\Comprehend\Comprehend.csproj'.
info : PackageReference for package 'AWSSDK.Comprehend' version '3.5.2.21' added to file 'C:\Amit Project\Programming-POC\C#\Practise\Fundamentals\aws-stuff\comprehend\src\Comprehend\Comprehend.csproj'.
info : Committing restore...
info : Generating MSBuild file C:\Amit Project\Programming-POC\C#\Practise\Fundamentals\aws-stuff\comprehend\src\Comprehend\obj\Comprehend.csproj.nuget.g.props.
info : Writing assets file to disk. Path: C:\Amit Project\Programming-POC\C#\Practise\Fundamentals\aws-stuff\comprehend\src\Comprehend\obj\project.assets.json
log  : Restored C:\Amit Project\Programming-POC\C#\Practise\Fundamentals\aws-stuff\comprehend\src\Comprehend\Comprehend.csproj (in 4.44 sec).
```

Without package install, was getting following error as it was not getting module.

```
C:\Amit Project\Programming-POC\C#\Practise\Fundamentals\aws-stuff\comprehend\src\Comprehend>dotnet build
Microsoft (R) Build Engine version 16.7.0+7fb82e5b2 for .NET
Copyright (C) Microsoft Corporation. All rights reserved.

  Determining projects to restore...
  Restored C:\Amit Project\Programming-POC\C#\Practise\Fundamentals\aws-stuff\comprehend\src\Comprehend\Comprehend.csproj (in 241 ms).
Sentiment.cs(2,14): error CS0234: The type or namespace name 'Comprehend' does not exist in the namespace 'Amazon' (are you missing an assembly reference?) [C:\Amit Project\Programming-POC\C#\Practise\Fundamentals\aws-stuff\comprehend\src\Comprehend\Comprehend.csproj]

Build FAILED.

Sentiment.cs(2,14): error CS0234: The type or namespace name 'Comprehend' does not exist in the namespace 'Amazon' (are you missing an assembly reference?) [C:\Amit Project\Programming-POC\C#\Practise\Fundamentals\aws-stuff\comprehend\src\Comprehend\Comprehend.csproj]
    0 Warning(s)
    1 Error(s)

```

#### Async call

Class has to be async as shared below..

```
public async Task getLanguage(){
    
}
```

Some of the task when are in async mode, we need to make that function in async mode.

```
DetectDominantLanguageResponse detectDominantLanguageResponse = await comprehendClient.DetectDominantLanguageAsync(detectDominantLanguageRequest);
```

Now async function call should be captured correctly.If I call like a sync call as shared below then will get error “*warning CS4014: Because this call is not awaited, execution of the current method continues before the call is completed. Consider applying the 'await' operator to the result of the call*”. Refer https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/compiler-messages/cs4014 for more details.

```
mycomprehend.getLanguage();
```

So in order to avoid such warning, we need to change the return of the async function return call as shared below…

- main caller function return now has been changed to async and it will return Task type
- Async function has been called with await so that compiler can understand.

```
namespace Comprehend
{
    class Program
    {
        static async Task Main(string[] args)
        {
            var mycomprehend = new Sentiment();
            Console.WriteLine("Hello Sentiment Class!");
            await mycomprehend.getLanguage();
        }
    }
}
```



#### Additional Permission

![1605895410485](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1605895410485.png)

### Unit Testing

- First I created test directory under my project comprehend and then created another folder Comprehend.Tests for having UT project. Here convention being followed is project name “Comprehend” followed by Test.
- Then create Unit testing project by dotnet new xunit
- Remember that, here comprehend is a collection of project and Comprehend is a specific project.

```

C:\Amit Project\Programming-POC\C#\Practise\Fundamentals\aws-stuff\comprehend\test\Comprehend.Tests>dotnet new xunit
The template "xUnit Test Project" was created successfully.

Processing post-creation actions...
Running 'dotnet restore' on C:\Amit Project\Programming-POC\C#\Practise\Fundamentals\aws-stuff\comprehend\test\Comprehend.Tests\Comprehend.Tests.csproj...
  Determining projects to restore...
  Restored C:\Amit Project\Programming-POC\C#\Practise\Fundamentals\aws-stuff\comprehend\test\Comprehend.Tests\Comprehend.Tests.csproj (in 962 ms).

Restore succeeded.


```

### Solution File

- It allows you to build source and test projects together
- See below, the solution file name is same as master directory one.
- Now, we need to add projects (source and test) into solution file.

```
C:\Amit Project\Programming-POC\C#\Practise\Fundamentals\aws-stuff\comprehend>dotnet new sln
The template "Solution File" was created successfully.

An update for template pack Microsoft.DotNet.Common.ItemTemplates::3.1.9 is available.
    install command: dotnet new -i Microsoft.DotNet.Common.ItemTemplates::5.0.0

C:\Amit Project\Programming-POC\C#\Practise\Fundamentals\aws-stuff\comprehend>ls -ltr
total 5
drwxr-xr-x 1 AKayal Domain Users   0 Nov 20 20:47 src
drwxr-xr-x 1 AKayal Domain Users   0 Nov 20 23:45 test
-rw-r--r-- 1 AKayal Domain Users 540 Nov 21 11:56 comprehend.sln
```

Here, I am adding s**ource and test project file together in solution file**.

```
C:\Amit Project\Programming-POC\C#\Practise\Fundamentals\aws-stuff\comprehend>dotnet sln add src\Comprehend\Comprehend.csproj
Project `src\Comprehend\Comprehend.csproj` added to the solution.

C:\Amit Project\Programming-POC\C#\Practise\Fundamentals\aws-stuff\comprehend>dotnet sln add test\Comprehend.Tests\Comprehend.Tests.csproj
Project `test\Comprehend.Tests\Comprehend.Tests.csproj` added to the solution.

C:\Amit Project\Programming-POC\C#\Practise\Fundamentals\aws-stuff\comprehend>
```

