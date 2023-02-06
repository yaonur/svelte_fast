<script>
    import { page } from '$app/stores';
    const navs = [
        {
            title: 'Home',
            href: '/'
        },
        {
            title: 'About',
            href: '/about'
        },
        {
            title: 'Services',
            href: '/services'
        },
        {
            title: 'Contact',
            href: '/contact'
        },
        {
            title: 'Dashboard',
            href: '/dashboard'
        },
        {
            title: 'Profile',
            href: '/profile'
        },
       {
            title: 'Login',
            href: '/login'
        }
    ];

    const setTheme = (theme) => {
      console.log(theme)
        document.documentElement.dataset.theme = theme;
        document.cookie = `siteTheme=${theme};max-age=31536000;path="/"`;
    };

    let routeId;
    $: routeId = $page.route.id;
</script>

<nav>
    <div class="container">
        <h1>Start</h1>
        <ul>
            {#each navs as { title, href }}
                <li class:active={routeId == href}><a {href} {title}>{title}</a></li>
            {/each}
            <li>
                <a href="#" on:click={() => setTheme('dark')}>Dark</a>
            </li>
                      <li>
                <a href="#" on:click={() => setTheme('light')}>Light</a>
            </li>

        </ul>
    </div>
</nav>

<style>
    nav {
        background-color: var(--navbar-background);
        color: var(--color-primary);
        /*padding: .5em;*/
    }

    ul {
        display: flex;
        list-style: None;
        margin-left: auto;
        font-size: 1.3em;
    }

    li {
        /*margin-right: 10px;*/
        padding: 0.5em 1em;
    }

    a {
        text-decoration: None;
        color: var(--color-primary);
    }

    li:hover {
        /*color: var(--color-primary-hover);*/
        background-color: #696969;
    }
    h1 {
        padding-left: 1em;
    }

    .container {
        display: flex;
        align-items: center;
    }

    .active {
        background-color: #3f3f3f;
    }

    .active a {
        /*color: #777676;*/
    }
</style>
