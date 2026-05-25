---
type: pc
class: "{[[class]]}"
ancestry: "{[[ancestry]]}"
heritage: "{[[heritage]]}"
background: "{[[background]]}"
level: "{level}"
hp: "{hp}"
ac: "{ac}"
modifier: "{initiative-modifier}"
skills:
  - "{skill +X}"
  - "{skill +X}"
feats:
  - "{[[feat]]}"
  - "{[[feat]]}"
equipment:
  - "{[[item]]}"
  - "{[[item]]}"
goal: "{goal}"
---
### `= this.file.name`
**Level** `= this.level` `= this.ancestry` `= this.class`
**Background** `= this.background`; **Heritage** `= this.heritage`
**HP** `= this.hp`; **AC** `= this.ac`; **Perception** +`= this.modifier`

{description}

#### Backstory

{backstory}

#### Character Development

**Current Goal** `= this.goal`

##### Key Events
> [!timeline|t-l]- **{development.title}** _{development.setting-date}_
> {development.description}
<!--  -->
> [!timeline|t-r]- **{development.title}** _{development.setting-date}_
> {development.description}

##### Development Ideas

- [ ] {development-idea}
- [ ] {development-idea}

#### Skills

``` dataview
```

#### Feats

``` dataview
```
``` dataview
LIST level
WHERE contains(file.outlinks, this.file.link) AND type = "feat"
```

#### Equipment

``` dataview

```
