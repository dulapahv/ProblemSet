void fill_1_column_top(int grid[4][4], int *top)
{
	int i;

	i = 0;
	while (i < 4)
	{
		if (top[i] == 1)
			grid[0][i] = 4;
		i++;
	}
}

void fill_1_column_bottom(int grid[4][4], int *bottom)
{
	int i;

	i = 0;
	while (i < 4)
	{
		if (bottom[i] == 1)
			grid[3][i] = 4;
		i++;
	}
}

void fill_1_row_left(int grid[4][4], int *left)
{
	int i;

	i = 0;
	while (i < 4)
	{
		if (left[i] == 1)
			grid[i][0] = 4;
		i++;
	}
}

void fill_1_row_right(int grid[4][4], int *right)
{
	int i;

	i = 0;
	while (i < 4)
	{
		if (right[i] == 1)
			grid[i][3] = 4;
		i++;
	}
}

void fill_1(int grid[4][4], int *top, int *bottom, int *left, int *right)
{
	fill_1_column_top(grid, top);
	fill_1_column_bottom(grid, bottom);
	fill_1_row_left(grid, left);
	fill_1_row_right(grid, right);
}