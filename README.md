# EazyDocs

eazydocs looks to provide an easy way to generate code documentation by cutting down repetitive boilerplate input. By providing a class or method object, you can generate a markdown (MD) file that mixes markdown and html formatting to clearly define your code.

## Getting started

- Install the eazydocs module using your preferred package manager:z
  ```
  pip install eazydocs
  ```
- Alternatively, the .whl can be downloaded and installed:
  ```
  pip install eazydocs-24.X.X-py3-none-any.whl
  ```

# Usage

- `eazydocs.generate_docs()`:
  - [Overview](#eazydocsgenerate_docs)
  - [Using a Class object](#using-a-class-object)
  - [Using a Method object](#using-a-method-object)
  - [Creating a MD File](#creating-a-md-file)
- `eazydocs.generate_example()`:

## eazydocs.generate_docs

<strong id='generate-docs'>generate_docs</strong>(<b>obj</b>, <b>append_to_file</b><i>=False</i>, <b>filename</b><i>=\_NoDefault.no_default</i>, <b>filepath</b><i>=\_NoDefault.no_default</i>)

> Parameters

<ul style='list-style: none'>
    <li>
        <b>obj : <i>object</i></b>
        <ul style='list-style: none'>
            <li>A Class or Method object.</li>
        </ul>
    </li>
    <li>
        <b>append_to_file : <i>bool, default False</i></b>
        <ul style='list-style: none'>
            <li>Append string output to a MD file.</li>
        </ul>
    </li>
    <li>
        <b>filename : <i>str, optional</i></b>
        <ul style='list-style: none'>
            <li>String expression of the markdown file to append. Required argument if <code>append_to_file=True</code>.</li>
        </ul>
    </li>
    <li>
        <b>filepath : <i>str, optional</i></b>
        <ul style='list-style: none'>
            <li>String expression of the absolute path to the markdown file you are appending. If <code>append_to_file=True</code>, and <code>filepath=None</code>, the <code>filename</code> is expected to be in the current working directory.</li>
        </ul>
    </li>
</ul>

### Using a Class object

- This example generates documents for the object `easydocs.Method`:

  ```
  >>> from eazydocs import generate_docs

  >>> docs = generate_docs(Method)
  >>> print(docs)

  <strong id='method'>Method</strong>(<b>method_name</b>)

  > Parameters

  <ul style='list-style: none'>
      <li>
          <b>method_name : <i>str</i></b>
          <ul style='list-style: none'>
              <li>{description}</li>
          </ul>
      </li>
  </ul>
  ```

- In a MD file, `docs` would appear as:
    <div style="border:1px solid gray; padding: 10px">
    <strong id='method'>Method</strong>(<b>method_name</b>)<br><br>

  > Parameters

    <ul style='list-style: none'>
        <li>
            <b>method_name : <i>str</i></b>
            <ul style='list-style: none'>
                <li>description</li>
            </ul>
        </li>
    </ul>
    </div>

* Notice the placeholder generated under the method name: 'description'. 

### Using a Method object

- This example generates documents for the object `eazydocs.generate_docs`:

  ```
    >>> from eazydocs import generate_docs

    >>> docs = generate_docs(generate_docs)
    >>> print(docs)

    <strong id='generate-docs'>generate_docs</strong>(<b>obj</b>, <b>append_to_file</b><i>=False</i>, <b>filename</b><i>=None</i>, <b>filepath</b><i>=None</i>)

    > Parameters

    <ul style='list-style: none'>
        <li>
            <b>obj : <i>object</i></b>
            <ul style='list-style: none'>
                <li>description</li>
            </ul>
        </li>
        <li>
            <b>append_to_file : <i>bool, default False</i></b>
            <ul style='list-style: none'>
                <li>description</li>
            </ul>
        </li>
        <li>
            <b>filename : <i>None | str, default None</i></b>
            <ul style='list-style: none'>
                <li>description</li>
            </ul>
        </li>
        <li>
            <b>filepath : <i>None | str, default None</i></b>
            <ul style='list-style: none'>
                <li>description</li>
            </ul>
        </li>
    </ul>
  ```

- In a MD file, this would appear as:
    <div style="border:1px solid gray; padding: 10px">
    <strong id='generate-docs'>generate_docs</strong>(<b>obj</b>, <b>append_to_file</b><i>=False</i>, <b>filename</b><i>=None</i>, <b>filepath</b><i>=None</i>)<br><br>

  > Parameters

    <ul style='list-style: none'>
        <li>
            <b>obj : <i>object</i></b>
            <ul style='list-style: none'>
                <li>description</li>
            </ul>
        </li>
        <li>
            <b>append_to_file : <i>bool, default False</i></b>
            <ul style='list-style: none'>
                <li>description</li>
            </ul>
        </li>
        <li>
            <b>filename : <i>None | str, default None</i></b>
            <ul style='list-style: none'>
                <li>description</li>
            </ul>
        </li>
        <li>
            <b>filepath : <i>None | str, default None</i></b>
            <ul style='list-style: none'>
                <li>description</li>
            </ul>
        </li>
    </ul>
    </div>

### Creating a MD file

- To create a MD file from `generate_docs` output, you can set its `append_to_file` to True. This will create a `README.md` file in your current working directory:

  ```
  >>> from eazydocs import generate_docs

  >>> generate_docs(Method, append_to_file=True)
  ```

- However, you may want to append the documents to an existing MD file, in which case you can provide the `filename`:

  ```
  >>> from eazydocs import generate_docs

  >>> generate_docs(
        Method,
        append_to_file=True,
        filename='METHOD'
      )
  ```

- Optionally, you can provide a `filepath` to the MD file, in addition to the `filename`:

  ```
  >>> from eazydocs import generate_docs

  >>> generate_docs(
        Method,
        append_to_file=True,
        filename='METHOD',
        filepath='~/$USER/eazydocs/output'
      )
  ```

  - The string argument provided to `filepath` is joined with `filename` as a pathlib.Path object

## eazydocs.generate_example
`eazydocs.generate_example` provides a simple method to format pandas.DataFrames and include examples in your README files. 