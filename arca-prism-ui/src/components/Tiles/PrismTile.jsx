import React from 'react';
import { Card } from '@ui5/webcomponents-react';
import { Icon } from '@ui5/webcomponents-react';
import { useNavigate } from 'react-router-dom';

const PrismTile = ({ title, icon, path }) => {
  const navigate = useNavigate();

  const tileStyle = {
    width: '150px',
    height: '150px',
    margin: '1rem',
    cursor: 'pointer',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    textAlign: 'center',
  };

  const iconStyle = {
    fontSize: '2rem',
    marginBottom: '1rem',
  };

  const handleClick = () => {
    navigate(path);
  };

  return (
    <Card style={tileStyle} onClick={handleClick}>
      <Icon name={icon} style={iconStyle} />
      <h4>{title}</h4>
    </Card>
  );
};

export default PrismTile;
