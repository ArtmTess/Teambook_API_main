import json
import pytest
import requests
from settings import VALID_EMAIL, VALID_PASSWORD


class TeamBookAPI:

    def __init__(self):
        self.base_url = 'https://web.teambooktest.com/api/'

    def get_token(self) -> json:
        """Request to get unique token by valid email and password"""
        data = {'user[email]': VALID_EMAIL,
                'user[password]': VALID_PASSWORD}
        res = requests.post(self.base_url + 'auth/login', data)
        my_token = (res.text.split('"')[1])
        my_status = res.status_code
        print(my_token)
        return my_token, my_status

    def create_project_required(self) -> json:
        """ Post method to create a new project with only required fields"""
        my_token = self.get_token()[0]
        data = {
            "name": "New_API_R951",
            "code": "R951",
            "color": "#EA8FEA",
            'active': True,
            "kind": "billable",
            "token": my_token
        }
        res = requests.post(self.base_url + 'projects', data=data)
        status = res.status_code
        project_id_r = res.json()
        project_id_r = project_id_r.get('id')
        print(project_id_r)
        return status, project_id_r

    def create_project(self) -> json:
        """ Post method to create a new project with all fields"""
        my_token = self.get_token()[0]
        data = {
            "name": "New_API951",
            "code": "Test951",
            "color": "#B9F3FC",
            'active': True,
            "kind": "billable",
            'icon_id': 1,
            'estimated': 80,
            'notes': 'test',
            'client_id': 5563,
            'manager_id': 9526,
            'status': 'Done',
            'business_unit': 'test',
            'token': my_token
        }
        res = requests.post(self.base_url + 'projects', data=data)
        status = res.status_code
        project_id = res.json()
        project_id = project_id.get('id')
        print(project_id)
        return status, project_id

    def deactivate_project(self, project_id) -> json:
        """ Request to deactivate a project """
        my_token = self.get_token()[0]
        project_id = self.create_project()[0]
        data = {
            'token': my_token,
            'project_ids[]': project_id
        }
        res = requests.patch(self.base_url + 'projects/deactivate', data=data)
        status = res.status_code
        print(project_id)
        return status

    def activate_project(self, project_id) -> json:
        """ Request to activate a project """
        my_token = self.get_token()[0]
        project_id = self.create_project()[0]
        data = {
            'token': my_token,
            'project_ids[]': project_id
        }
        res = requests.patch(self.base_url + 'projects/activate', data=data)
        status = res.status_code
        print(project_id)
        return status

    def delete_project(self, project_id) -> json:
        """ Request to delete a project """
        my_token = self.get_token()[0]
        project_id = self.create_project()[0]
        data = {
            'token': my_token,
            'project_ids[]': project_id
        }
        res = requests.patch(self.base_url + 'projects/delete', data=data)
        status = res.status_code
        return status

    def get_all_projects(self) -> json:
        """ Request to get a list of all projects """
        my_token = self.get_token()[0]
        res = requests.get(self.base_url + 'projects' + '?token=' + my_token)
        status = res.status_code
        return status

    def get_active_projects(self) -> json:
        """ Request to get a list of active projects """
        my_token = self.get_token()[0]
        res = requests.get(self.base_url + 'projects/active' + '?token=' + my_token)
        status = res.status_code
        return status

    def get_deactivated_projects(self) -> json:
        """ Request to get a list of deactivated projects """
        my_token = self.get_token()[0]
        res = requests.get(self.base_url + 'projects/deactivated' + '?token=' + my_token)
        status = res.status_code
        return status

    def get_business_units(self) -> json:
        """ Request a list of business units """
        my_token = self.get_token()[0]
        res = requests.get(self.base_url + 'projects/business_units' + '?token=' + my_token)
        status = res.status_code
        return status

    def get_managers(self) -> json:
        """ Request a list of managers """
        my_token = self.get_token()[0]
        res = requests.get(self.base_url + 'projects/managers' + '?token=' + my_token)
        status = res.status_code
        return status
