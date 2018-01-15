import React, { Component } from 'react'
import { hostname } from '../shared/constants'

class Main extends Component {
    constructor(props) {
        super(props)
        this.state = {
            status: -1
        }
    }

    onClick() {
        var input = document.querySelector('input[type="file"]')
        var data = new FormData()
        data.append('file', input.files[0])
        fetch(hostname + '/api/v1/upload', {
            method: 'POST',
            body: data
        }).then(resp => {
            if (resp.status === 400) {
                this.setState({ status: 1 })
            } else {
                this.setState({ status: 0 })
            }
        })
    }

    render() {
        const { status, message } = this.state
        return (
            <div className="home">
                <div className="container">
                    <div className="content">
                        <div className="title">
                            ხელწერის ნიმუშების შეგროვება
                        </div>
                        <p>მინდა შეიქმნას ქართული ასოების დეტასეტი რომ მომავალში იყოს ასოების ამომცობის გაწვრთნა შესაძლებელი.</p>
                        <h2>1. ჩამოვტვირთოთ შესავსები დოკუმენტი: <a
                            href="https://github.com/TornikeNatsvlishvili/writing.skivri.ge/raw/master/Georgian%20Training%20Input%20Sheet.pdf"
                            download>ჩამოტვირთვა</a></h2>
                        <h2>2. ამობეჭდეთ ჩამოტვირთული დოკუმენტი</h2>
                        <h2>3. შვავსოთ სათითაო უჯრედი:</h2>
                        <div className="example">
                            <img src="/images/sample.png" />
                            <h2>ჩაეტიეთ უჯრედებში!</h2>
                        </div>
                        <h2>4. დავაკანიროთ ან სურათი გადავუღოთ შევსებულ დოკუმენტს</h2>
                        <h2 className="spread-out">
                            <span>5. ავტვირთოთ:</span>
                            <form encType="multipart/form-data">
                                <input className="path" type="file" name="file" />
                            </form>
                        </h2>
                        <div className="center">
                            <button onClick={() => this.onClick()} className="btn upload-btn">Upload</button>
                            {status === 0 && <h1 className="success">მიღებულია! &hearts;</h1>}
                            {status === 1 && <h1 className="error">ვერ აიტვრითა!</h1>}
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default Main