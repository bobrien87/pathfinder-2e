---
type: npc
title: "{title}"
faction: "{[[faction]]}"
occupation: "{occupation}"
goal: "{goal}"
attitude: "{[[condition]]}"
location: "{[[location]]}"
homeland: "{[[location]]}"
ancestry: "{[[ancestry]]}"
alignment: "{[[alignment|abbreviation]]}"
accent: "{accent}"
quirk: "{quirk}"
mannerism: "{mannerism}"
secrets:
  - "{wikilink:discovery}"
  - "{wikilink:discovery}"
---
### `= this.file.name`
**`= this.title`**
`= choice(this.alignment != null, this.alignment + " ", "") + this.ancestry` `= choice(this.homeland != null, "(" + this.homeland + ")", "")` `= this.occupation` `= choice(this.faction != null, "(" + this.faction + ")", "")`
**Goal** `= this.goal`
**Attitude** `= this.attitude`
**Location** `= this.location`
`= choice(this.accent != null, "**Accent** " + this.accent + choice(this.mannerism != null, ";", ""), "")` `= choice(this.mannerism != null, "**Mannerism** " + this.mannerism, "")`
`= choice(this.quirk != null, "**Quirk** " + this.quirk, "")`

{description}

#### Secrets

``` dataview
LIST WITHOUT ID secret
WHERE file.path = this.file.path
FLATTEN this.secrets as secret
```

#### Character Development

> [!timeline|t-l]- **{development.title}** _{development.setting-date}_
> {development.description}
<!--  -->
> [!timeline|t-r]- **{development.title}** _{development.setting-date}_
> {development.description}

##### Development Ideas

- [ ] {development-idea}
- [ ] {development-idea}

#### Encounters
``` encounter
name: {encounter.name}
party: {party}
creatures:
  - 1: {npc}
  - 2: {minion}
```