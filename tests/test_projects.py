from API.api import TeamBookAPI

projects = TeamBookAPI()


def test_get_token():
    status = projects.get_token()[1]
    token = projects.get_token()[0]
    assert status == 201
    assert token


def test_create_project_required():
    data = projects.create_project_required()
    status = data[0]
    project_id_r = data[1]
    assert status == 201
    assert project_id_r


def test_create_project():
    data = projects.create_project()
    status = data[0]
    project_id = data[1]
    assert status == 201
    assert project_id


def test_deactivate_project():
    project_id = projects.create_project()[1]
    status = projects.deactivate_project(project_id)
    projects.delete_project(project_id)
    assert status == 200


def test_activate_project():
    project_id = projects.create_project()[1]
    projects.deactivate_project(project_id)
    status = projects.activate_project(project_id)
    projects.delete_project(project_id)
    assert status == 200


def test_delete_project():
    project_id = projects.create_project()[1]
    status = projects.delete_project(project_id)
    assert status == 200


def test_get_all_projects():
    status = projects.get_all_projects()
    assert status == 200


def test_get_active_projects():
    status = projects.get_active_projects()
    assert status == 200


def test_get_deactivated_projects():
    status = projects.get_deactivated_projects()
    assert status == 200


def test_get_business_units():
    status = projects.get_business_units()
    assert status == 200


def test_get_managers():
    status = projects.get_managers()
    assert status == 200
