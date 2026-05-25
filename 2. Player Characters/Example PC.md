---
type: pc
portrait: "[[example-pc.png]]"
class: "[[Bard]]"
ancestry: "[[Elf]]"
heritage: "[[Seer Elf]]"
background: "[[Entertainer]]"
level: "3"
hp: "26"
ac: "14"
modifier: "3"
skills: Acrobatics +3
feats:
  - "{[[feat]]}"
  - "{[[feat]]}"
equipment:
  - "{[[item]]}"
  - "{[[item]]}"
goal: Find her half brother
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
