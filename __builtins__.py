# pylint: disable-all
from __future__ import annotations

from typing import Any, Callable, Sequence

from py4j.java_gateway import JavaClass, JavaObject
from pyspark.context import SparkContext
from pyspark.sql.context import SQLContext
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.session import SparkSession
from pyspark.sql.types import DataType, StringType

sc: SparkContext

sqlContext: SQLContext


def table(self, tableName: str) -> DataFrame:
    ...


def sql(self, sqlQuery: str) -> DataFrame:
    ...


def udf(f: Callable = None, returnType: DataType | str = StringType()) -> Callable:
    ...


def display(self, input=None, *args, **kwargs) -> None:
    ...


def displayHTML(self, html) -> None:
    ...


def getArgument(self, name, defaultValue=None) -> Any:
    ...


class _DBUtils:
    class JobsHandler:
        entry_point: JavaObject
        taskValues: _DBUtils.JobsHandler.TaskValuesHandler
        displayHTML: displayHTML

        def __init__(self, entry_point, displayHTML) -> None:
            ...

        def help(self, method_name: str = ...) -> None:
            ...

        def __call__(self) -> _DBUtils.JobsHandler:
            ...

        class TaskValuesHandler:
            entry_point: JavaObject
            displayHTML: displayHTML

            def __init__(self, entry_point, displayHTML) -> None:
                ...

            def get(
                self,
                taskKey,
                key,
                default: Any | None = ...,
                debugValue: Any | None = ...,
            ) -> Any:
                ...

            def set(self, key, value) -> None:
                ...

            def help(self, method_name: str = ...) -> None:
                ...

            def __call__(self) -> _DBUtils.JobsHandler.TaskValuesHandler:
                ...

    class NotebookHandler:
        shell: Any
        entry_point: JavaObject
        sc: SparkContext
        displayHTML: displayHTML

        def __init__(self, shell, entry_point, displayHTML, sc) -> None:
            ...

        def __call__(self) -> _DBUtils.NotebookHandler:
            ...

        def help(self, method_name: str = ...) -> None:
            ...

        def exit(self, value) -> None:
            ...

        def run(
            self,
            path,
            timeout_seconds: int,
            arguments=...,
            __databricks_internal_cluster_spec: Any | None = ...,
        ) -> str:
            ...

    class PreviewHandler:
        secret: _DBUtils.SecretsHandler

        def __init__(self, secret) -> None:
            ...

    class SecretsHandler:
        entry_point: JavaObject
        displayHTML: displayHTML

        def __init__(self, entry_point, displayHTML) -> None:
            ...

        def __call__(self) -> _DBUtils.SecretsHandler:
            ...

        def help(self, method_name: str | None = ...) -> None:
            ...

        def create_list_from_jschema(self, jschema, create_obj_from_jschema):
            ...

        def get(self, scope, key) -> str:
            ...

        def getBytes(self, scope, key) -> bytearray:
            ...

        def list(self, scope) -> Sequence:
            ...

        def listScopes(self) -> Sequence:
            ...

    class CredentialsHandler:
        entry_point: JavaObject
        displayHTML: displayHTML

        def __init__(self, entry_point, displayHTML) -> None:
            ...

        def __call__(self) -> _DBUtils.CredentialsHandler:
            ...

        def help(self, method_name: str | None = ...) -> None:
            ...

        def assumeRole(self, role) -> bool:
            ...

        def showCurrentRole(self) -> list:
            ...

        def showRoles(self) -> list:
            ...

        def getCurrentCredentials(self) -> dict | None:
            ...

    class LibraryHandler:
        entry_point: JavaObject
        sc: SparkContext
        displayHTML: displayHTML

        def __init__(self, sc, entry_point, displayHTML) -> None:
            ...

        def __call__(self) -> _DBUtils.LibraryHandler:
            ...

        def print_and_return(self, result) -> bool:
            ...

        def print_dbutils_library_deprecation_message(self, should_error: bool = ...) -> None:
            ...

        def help(self, method_name: str | None = ...) -> None:
            ...

        def install(self, path) -> bool:
            ...

        def installPyPI(self, project, version: str = ..., repo: str = ..., extras: str = ...) -> bool:
            ...

        def restartPython(self) -> None:
            ...

        def list(self) -> list:
            ...

    class FSHandler:
        fsutils: JavaClass
        dbcore: JavaObject
        fsutils_parallel: JavaObject
        sc: SparkContext
        entry_point: JavaObject
        displayHTML: displayHTML

        def __init__(self, fsutils, fsutils_parallel, dbcore, sc, entry_point, displayHTML) -> None:
            ...

        def __call__(self) -> _DBUtils.FSHandler:
            ...

        def print_return(self, result) -> bool:
            ...

        def check_types(self, vars_and_types) -> None:
            ...

        def help(self, method_name: str | None = ...) -> None:
            ...

        def create_list_from_jschema(self, jschema, create_obj_from_jschema):
            ...

        def prettify_exception_message(f) -> _DBUtils.FSHandler:
            ...

        def should_use_parallel_dbutils_fs(self) -> bool:
            ...

        def cp(self, source, dest, recurse: bool = ...) -> bool:
            ...

        def head(self, file, max_bytes: int = ...) -> str:
            ...

        def ls(self, path) -> Sequence:
            ...

        def mkdirs(self, dir) -> bool:
            ...

        def mv(self, source, dest, recurse: bool = ...) -> bool:
            ...

        def put(self, file, contents, overwrite: bool = ...) -> bool:
            ...

        def rm(self, dir, recurse: bool = ...) -> bool:
            ...

        def cacheFiles(self, *files) -> bool:
            ...

        def cacheTable(self, name) -> bool:
            ...

        def uncacheFiles(self, *files) -> bool:
            ...

        def uncacheTable(self, name) -> bool:
            ...

        def mount(
            self,
            source,
            mount_point,
            encryption_type: str = ...,
            owner: Any | None = ...,
            extra_configs=...,
        ) -> bool:
            ...

        def updateMount(
            self,
            source,
            mount_point,
            encryption_type: str = ...,
            owner: Any | None = ...,
            extra_configs=...,
        ) -> bool:
            ...

        def mounts(self) -> bool:
            ...

        def refreshMounts(self) -> bool:
            ...

        def unmount(self, mount_point) -> bool:
            ...

    sc: SparkContext
    sqlContext: SQLContext
    entry_point: JavaObject
    displayHTML: displayHTML

    def __init__(self, py_shell, entry_point, sc, sqlContext, displayHTML) -> None:
        ...

    class DataHandler:
        entry_point: JavaObject
        displayHTML: displayHTML
        sqlContext: SQLContext

        def __init__(self, entry_point, displayHTML, sqlContext) -> None:
            ...

        def __call__(self) -> _DBUtils.DataHandler:
            ...

        def help(self, method_name: str | None = ...) -> None:
            ...

        def summarize(self, df, precise: bool = ...) -> None:
            ...

    class WidgetsHandlerImpl:
        displayHTML: displayHTML

        def __init__(self, jvm, entry_point, displayHTML) -> None:
            ...

        def help(self, method_name: str = ...) -> None:
            ...

        def get(self, name) -> str:
            ...

        def getArgument(self, name, defaultValue: Any | None = ...) -> str:
            ...

        def text(self, name, defaultValue, label: str | None = ...) -> None:
            ...

        def dropdown(self, name, defaultValue, choices, label: str | None = ...) -> None:
            ...

        def combobox(self, name, defaultValue, choices, label: str | None = ...) -> None:
            ...

        def multiselect(self, name, defaultValue, choices, label: str | None = ...) -> None:
            ...

        def remove(self, name) -> None:
            ...

        def removeAll(self) -> None:
            ...

    @property
    def shell(self) -> Any:
        ...

    fs: FSHandler
    jobs: JobsHandler
    notebook: NotebookHandler
    secrets: SecretsHandler
    preview: PreviewHandler
    widgets: WidgetsHandlerImpl
    library: LibraryHandler
    credentials: CredentialsHandler
    data: DataHandler

    def help(self, method_name: str = ...) -> None:
        ...


dbutils: _DBUtils

spark: SparkSession

In: list

Out: dict


def get_ipython():
    ...


class exit:
    rewrite: bool

    def set_ip(ip):
        ...


class quit:
    rewrite: bool

    def set_ip(ip):
        ...
