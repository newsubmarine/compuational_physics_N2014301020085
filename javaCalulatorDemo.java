package calculator3;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.Window;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JTextField;  

public class Calculator extends JFrame implements ActionListener{
	private static final long serialVersionUID = 1578930017076412511L;
	
	  
	private JMenu jmenuFile, jmenuHelp;
	private JMenuItem jmenuitemExit, jmenuitemAbout;
	
	private JTextField textResult;
	private JButton jButtons[];
	private JPanel jplMaster, jplBackSpace, jplControl,jplButtons;
	// 设置变量
		 private boolean firstString = true;  	     
		 private double resultNum=0.0;  	   
		 private String operator="=";    
		 private boolean operateValid = true;  
	// Constructor 
	public Calculator() 
	{
		//设置菜单栏
		jmenuFile = new JMenu("File");		
		jmenuitemExit = new JMenuItem("Exit");
		jmenuFile.add(jmenuitemExit);
		jmenuHelp = new JMenu("Help");
		jmenuitemAbout = new JMenuItem("About Calculator");//About
		jmenuHelp.add(jmenuitemAbout);	
		JMenuBar mb = new JMenuBar();
		mb.add(jmenuFile);
		mb.add(jmenuHelp);
		setJMenuBar(mb);
		
		//设置显示结果的文本框
		setBackground(Color.gray);
		jplMaster = new JPanel();
		textResult = new JTextField("0");
		textResult.setHorizontalAlignment(JTextField.RIGHT); 
		textResult.setEditable(false);  
	    textResult.setBackground(Color.white);  
		
		// Add components to frame
		getContentPane().add(textResult, BorderLayout.NORTH);

		jButtons = new JButton[19];
		jplButtons = new JPanel();			// 构造按钮容器

		//数字符0~9的按钮
		for (int i=0; i<=9; i++)
		{
			jButtons[i] = new JButton(String.valueOf(i));
		}

		//创建操作按钮
		jButtons[10] = new JButton(".");
		jButtons[11] = new JButton("/");
		jButtons[12] = new JButton("*");
		jButtons[13] = new JButton("-");
		jButtons[14] = new JButton("+");
		jButtons[15] = new JButton("sqrt");		
		jplBackSpace = new JPanel();//退格键
		jplBackSpace.setLayout(new GridLayout(1, 1, 5, 5));

		jButtons[16] = new JButton("Backspace");
		jplBackSpace.add(jButtons[16]);

		jplControl = new JPanel();
		jplControl.setLayout(new GridLayout(1,2, 5 ,5));
		
		jButtons[17] = new JButton("=");
		jButtons[18] = new JButton("C");
		jplControl.add(jButtons[17]);
		jplControl.add(jButtons[18]);

		//	设置数字键为蓝色，其他键为绿色
		for (int i=0; i<jButtons.length; i++)	{

			if (i<10)
				jButtons[i].setForeground(Color.blue);
				
			else
				jButtons[i].setForeground(Color.red);
		}	
		jplButtons.setLayout(new GridLayout(4, 4, 5, 5));
		//在jplButton上添加按钮
		// 第一行
		for(int i=7; i<=9; i++)		{
			jplButtons.add(jButtons[i]);
		}	
		//按钮“/”
		jplButtons.add(jButtons[11]);
		// 第二行
		for(int i=4; i<=6; i++)
		{
			jplButtons.add(jButtons[i]);
		}		
		// 按钮“*”
		jplButtons.add(jButtons[12]);
		//第三行
		for( int i=1; i<=3; i++)
		{
			jplButtons.add(jButtons[i]);
		}	
		//按钮“-”
		jplButtons.add(jButtons[13]);
		//第四行
		//按钮 0, ., sqrt, =
		jplButtons.add(jButtons[0]);
		jplButtons.add(jButtons[10]);
		jplButtons.add(jButtons[15]);
		jplButtons.add(jButtons[14]);
		//退格键居左;=，C居右，按钮居下
		jplMaster.setLayout(new BorderLayout());
		jplMaster.add(jplBackSpace, BorderLayout.WEST);
		jplMaster.add(jplControl, BorderLayout.EAST);
		jplMaster.add(jplButtons, BorderLayout.SOUTH);
		//把面板添加进容器，居下
		getContentPane().add(jplMaster, BorderLayout.SOUTH);
		//添加事件处理接口
		for (int i=0; i<jButtons.length; i++){
			jButtons[i].addActionListener(this);
		}
		jmenuitemAbout.addActionListener(this);
		jmenuitemExit.addActionListener(this);
	}
	public void actionPerformed(ActionEvent e) {  
		String s = e.getActionCommand();//得到所按键的字符，便于处理数字“类”和运算键“类”的方法
		if(e.getSource() == jmenuitemAbout){
			JDialog dlgAbout = new CustomABOUTDialog(this, "About Java Calculator", true);
			dlgAbout.setVisible(true);
		}else if(e.getSource() == jmenuitemExit){
			System.exit(0);
			}if (e.getSource() == jButtons[16] ){  
            // 用户按了"Backspace"键  
            backspaceDisplay();  
        }  else if (e.getSource()==jButtons[18]) {  
            // 用户按了"C"键  
            clearAll();  
        } 
        else if ("0123456789.".indexOf(s) >= 0) {  
            // 用户按了数字键或者小数点键  
           numberDisplay(s);  
        } else {  
            // 用户按了运算符键  
            operatorDisplay(s);  
        }  
    }  

    // 按下退格键的方法
    private void backspaceDisplay() {  
        String text = textResult.getText();  
        int i = text.length();  
        if (i > 0) {  
            // 退格，将文本最后一个字符去掉  
            text = text.substring(0, i - 1);  
            if (text.length() == 0) {  
                // 如果文本没有了内容，则初始化计算器的各种值  
                textResult.setText("0");  
                firstString = true;  
                operator = "=";  
            } else {  
                // 显示新的文本  
                textResult.setText(text);  
            }  
        }  
    }  
  
    //按下数字键的方法  
    private void numberDisplay(String s) {  
        if (firstString) {  
            // 输入的第一个数字  
            textResult.setText(s);  
        } else if ((s.equals(".")) && (textResult.getText().indexOf(".") < 0)) {  
            // 判断之前有无小数点，如果有则不能再添加小数点
        	textResult.setText(textResult.getText() + ".");  
        	//输入的是数字，直接加在文本后面
        } else if (!s.equals(".")) {  
            textResult.setText(textResult.getText() + s);  
        }    
        firstString = false; 
    }  
  
    /** 
     * 处理C键被按下的事件 
     */  
    private void clearAll() {  

        textResult.setText("0");  
        firstString = true;  
        operator = "=";  
    }  
  
    //按下运算符的方法  
    private void operatorDisplay(String key) {  
        if (operator.equals("/")) {  
            // 除法运算  
            // 如果当前结果文本框中的值等于0  
            if (getNumberFromText() == 0.0) {  
                // 操作不合法  
                operateValid = false;  
                textResult.setText("Cannot divide by zero!");  
            } else {  
                resultNum /= getNumberFromText();  
            }  
        }  else if (operator.equals("+")) {  
            // 加法  
            resultNum += getNumberFromText();  
        } else if (operator.equals("-")) {  
            // 减法  
            resultNum -= getNumberFromText();  
        } else if (operator.equals("*")) {  
            // 乘法  
            resultNum *= getNumberFromText();  
        } else if (operator.equals("sqrt")) {  
            // 平方  
            resultNum = Math.sqrt(resultNum);//调用了Math中的方法 
        }else if (operator.equals("=")) {  
            // 赋值  
            resultNum = getNumberFromText();  
        }  
        if (operateValid) {  
            // 双精度浮点数的运算，当结果是int型时不会转换成double型
            long t1;  
            double t2; //判断运算是否损失精度 
            t1 = (long) resultNum;  
            t2 = resultNum - t1;  
            if (t2 == 0) {  
                textResult.setText(String.valueOf(t1));  
            } else {  
                textResult.setText(String.valueOf(resultNum));  
            }  
        }  
        // 运算符等于用户按的按钮  
        operator = key;  
        firstString = true;  
        operateValid = true;  
    }  
  
    // 从结果文本框中获取数字 
      
    private double getNumberFromText() {  
        double result = 0;  
        try {  
            result = Double.valueOf(textResult.getText()).doubleValue();  
        } catch (NumberFormatException e) {  
        }  
        return result;  
    }  
  
    public static void main(String args[]) {  
    	Calculator calculator1 = new Calculator();  
        calculator1.setVisible(true);  
        calculator1.setTitle("Java Calculator");
        calculator1.setSize(240,180);
        calculator1.pack();
        calculator1.setLocation(400, 250);
		calculator1.setVisible(true);
		calculator1.setResizable(true);
    }  
} 
class CustomABOUTDialog extends JDialog implements ActionListener {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	CustomABOUTDialog(JFrame parent, String title, boolean modal){
		super(parent, title, modal);
		setBackground(Color.black);
		
		JPanel p1 = new JPanel(new FlowLayout(FlowLayout.CENTER));
		StringBuffer text = new StringBuffer();
		text.append("Calculator Information\n\n");
		text.append("Version:	3.0");
		
		JTextArea jtAreaAbout = new JTextArea();
		jtAreaAbout.setText(text.toString());
		jtAreaAbout.setEditable(false);

		p1.add(jtAreaAbout);
		p1.setBackground(Color.white);
		getContentPane().add(p1, BorderLayout.CENTER);

		setLocation(408, 270);
		setResizable(false);

		addWindowListener(new WindowAdapter() {
				public void windowClosing(WindowEvent e)
				{
					Window aboutDialog = e.getWindow();
					aboutDialog.dispose();
				}
			}
		);
		pack();
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		
	}
}

		
