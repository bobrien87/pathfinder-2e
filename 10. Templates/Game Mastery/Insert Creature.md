---
type: creature
group: ["{group_01}", "{group_02}"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "{name}"
level: "{level}"
rare_01: "{rare_01}"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: "{alignment}"
size: "{size}"
trait_01: "{trait_01}"
trait_02: "{trait_02}"
trait_03: "{trait_03}"
trait_04: "{trait_04}"
trait_05: "{trait_05}"
trait_06: "{trait_06}"
trait_07: "{trait_07}"
perception:
  - name: Perception
    desc: "{perception}"
languages: "{languages}"
skills:
  - name: Skills
    desc: "{skills}"
abilityMods:
  - "{ability_str}"
  - "{ability_dex}"
  - "{ability_con}"
  - "{ability_int}"
  - "{ability_wis}"
  - "{ability_cha}"
abilities_top:
  - name: "{ability_top_name}"
    desc: "{ability_top_desc}"
armorclass:
  - name: AC
    desc: "{ac}; **Fort** {fort}, **Ref** {ref}, **Will** {will}"
health:
  - name: HP
    desc: "{hp}"
abilities_mid:
  - name: "{ability_mid_name}"
    desc: "{ability_mid_desc}"
speed: "{speed}"
attacks:
  - name: "{attack_name}"
    desc: "{attack_desc}"
spellcasting:
  - name: "{spellcasting_name}"
    desc: "{spellcasting_desc}"
abilities_bot:
  - name: "{ability_bot_name}"
    desc: "{ability_bot_desc}"
sourcebook: "{source}"
source-type: "{source-type}"
---
### `= this.file.name`

{description}

```statblock
creature: "{name}"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
