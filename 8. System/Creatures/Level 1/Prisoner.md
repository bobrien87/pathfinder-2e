---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Prisoner"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +6, Intimidation +3, Stealth +7, Thievery +7"
abilityMods: ["+3", "+4", "+1", "+0", "+1", "+0"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The prisoner does an extra 1d6 precision damage to [[Off Guard]] creatures."
  - name: "Surprise Attack"
    desc: "On the first round of combat, creatures that haven't acted yet are [[Off Guard]] to the prisoner."
armorclass:
  - name: AC
    desc: "16; **Fort** +4, **Ref** +9, **Will** +6"
health:
  - name: HP
    desc: "17"
abilities_mid:
  - name: "You're Next"
    desc: "`pf2:r` **Trigger** The prisoner reduces a creature to 0 hit points. <br>  <br> **Effect** The prisoner attempts an Intimidation check with a +2 circumstance bonus to `act demoralize options=youre-next` a single creature it can see and that can see them."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shiv +7 (`pf2:1`) (agile), **Damage** 1d4+3 piercing"
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Most who end up in a jail, dungeon, or prison are just biding their time until their imprisonment ends, trying to find ways to make it through interminable days of boredom and deprivation. Some, however, may use their time on the inside to strengthen their criminal connections. Using force and intimidation to gain status among other prisoners, they create makeshift weapons to take down their enemies and give them an edge if escape becomes possible. Even for prisoners who don't become involved in the world of prison politics, learning to stand up for themselves and projecting an air of toughness can become essential for survival in a place where people have little left to lose.

Unfortunately, every society has people living on its fringes. While good communities work to grant aid and respite to their downtrodden, sometimes-due to economic downturn, famine, or war-the ranks of the less fortunate exceed the community's capacity to support them. In heartless neutral and evil societies, poverty is seen as an inevitability that can never be truly eradicated, or even worse, as a tool to be manipulated for political gain.

```statblock
creature: "Prisoner"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
