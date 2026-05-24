---
type: pc
class: "{[[class]]}"
ancestry: "{[[ancestry]]}"
heritage: "{heritage}"
background: "{[[background]]}"
level: "{level}"
hp: "{hp}"
ac: "{ac}"
party: "{[[party]]}"
---
### `= this.file.name`
**Level** `= this.level` `= this.ancestry` `= this.class`
**Background** `= this.background` | **Heritage** `= this.heritage`
**HP** `= this.hp` | **AC** `= this.ac` | **Party** `= this.party`

***

{description}

#### Attributes & Skills
{attributes-and-skills}

#### Feats & Abilities
``` dataview
LIST level
WHERE contains(file.outlinks, this.file.link) AND type = "feat"
```

#### Equipment & Inventory
{inventory}
