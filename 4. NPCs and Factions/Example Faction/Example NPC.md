---
type: npc
title: Lord Commander
faction: "[[Example Faction]]"
occupation: Commander
goal: Destroy the orc horde
attitude: "[[Friendly]]"
location: "[[Example Location]]"
homeland: "[[Example Location]]"
ancestry: "[[Human]]"
alignment: "[[Lawful Good|LG]]"
accent: Posh
mannerism: Prone to staring into the distance
quirk: Survived orc massacre at [[Example Location]]
secrets:
  - "[[Example Discovery]]"
---
### `= this.file.name`
**`= this.title`**
`= choice(this.alignment != null, this.alignment + " ", "") + this.ancestry` `= choice(this.homeland != null, "(" + this.homeland + ")", "")` `= this.occupation` `= choice(this.faction != null, "(" + this.faction + ")", "")`
**Goal** `= this.goal`
**Attitude** `= this.attitude`
**Location** `= this.location`
`= choice(this.accent != null, "**Accent** " + this.accent, "")`, `= choice(this.mannerism != null, "**Mannerism** " + this.mannerism, "")`
`= choice(this.quirk != null, "**Quirk** " + this.quirk, "")`

Tall, dashing, handsome. Large, full moustache. He carries himself as one who has seen loss and adversity.

#### Secrets

``` dataview
LIST WITHOUT ID secret
WHERE file.path = this.file.path
FLATTEN this.secrets as secret
```

#### Character Development

> [!timeline|t-l]- **Survived massacre at Location** _3 Desnus 4730_
> As a child, Example NPC was the sole survivor of a brutal orc raid on Location. His family were found hung and his little brother's body was never found.
<!--  -->
> [!timeline|t-r]- **Promoted to Lord Commander** _22 Desnus 4764_
> After leading the defence against the orc siege, Example NPC was promoted to the rank of Lord Commander.

##### Development Ideas

- [ ] Word reaches the Lord Commander that his younger brother may yet be alive, kept as a slave by the orcs

#### Encounters
``` encounter
name: {encounter.name}
party: {party}
creatures:
  - 1: {npc}
  - 2: {minion}
```