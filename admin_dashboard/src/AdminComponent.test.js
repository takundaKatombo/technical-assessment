
// admin_dashboard/src/components/AdminComponent.test.js
import React from 'react';
import { render, screen } from '@testing-library/react';
import AdminComponent from './AdminComponent';

test('renders admin component', () => {
    render(<AdminComponent />);
    expect(screen.getByText(/admin/i)).toBeInTheDocument();
});
