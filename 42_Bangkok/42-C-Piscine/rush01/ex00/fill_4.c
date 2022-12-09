void fill_4_column_top(int grid[4][4], int *top)
{
	int i;

	i = 0;
	while (i < 4)
	{
		if (top[i] == 4)
		{
			grid[0][i] = 1;
			grid[1][i] = 2;
			grid[2][i] = 3;
			grid[3][i] = 4;
		}
		i++;
	}
}

void fill_4_column_bottom(int grid[4][4], int *bottom)
{
	int i;

	i = 0;
	while (i < 4)
	{
		if (bottom[i] == 4)
		{
			grid[0][i] = 4;
			grid[1][i] = 3;
			grid[2][i] = 2;
			grid[3][i] = 1;
		}
		i++;
	}
}

void fill_4_row_left(int grid[4][4], int *left)
{
	int i;

	i = 0;
	while (i < 4)
	{
		if (left[i] == 4)
		{
			grid[i][0] = 1;
			grid[i][1] = 2;
			grid[i][2] = 3;
			grid[i][3] = 4;
		}
		i++;
	}
}

void fill_4_row_right(int grid[4][4], int *right)
{
	int i;

	i = 0;
	while (i < 4)
	{
		if (right[i] == 4)
		{
			grid[i][0] = 4;
			grid[i][1] = 3;
			grid[i][2] = 2;
			grid[i][3] = 1;
		}
		i++;
	}
}

void fill_4(int grid[4][4], int *top, int *bottom, int *left, int *right)
{
	fill_4_column_top(grid, top);
	fill_4_column_bottom(grid, bottom);
	fill_4_row_left(grid, left);
	fill_4_row_right(grid, right);
}