---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Accuser Agent"
level: "9"
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
    desc: "+19"
languages: "Common (up to 3 additional languages)"
skills:
  - name: Skills
    desc: "Deception +20, Diplomacy +18, Intimidation +18, Society +18, Stealth +17, Thievery +19, Legal Lore +20"
abilityMods: ["+0", "+4", "+0", "+3", "+4", "+3"]
abilities_top:
  - name: "+2 to Sense Motive"
    desc: ""
  - name: "Insightful"
    desc: "When the accuser agent succeeds at a Perception check, they critically succeed instead."
  - name: "Debilitating Sneak Attack"
    desc: "The accuser agent's Strikes deal an extra 3d6 precision damage to [[Off Guard]] creatures. A target who takes this additional precision damage also either becomes [[Enfeebled]] 1 or takes a –10-foot status penalty to its Speeds until the end of the agent's next turn. <br>  <br> > [!danger] Effect: Debilitating Sneak Attack"
armorclass:
  - name: AC
    desc: "28; **Fort** +15, **Ref** +19, **Will** +19"
health:
  - name: HP
    desc: "115"
abilities_mid:
  - name: "Objection!"
    desc: "`pf2:r` **Trigger** A creature within 30 feet takes an action with the linguistic trait <br>  <br> **Effect** The triggering creature must succeed a DC 28 [[Will]] save saving throw or their action is disrupted."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +20 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+8 bludgeoning"
  - name: "Melee strike"
    desc: "Dagger +20 (`pf2:1`) (agile, deadly d6, finesse, magical, versatile s), **Damage** 2d4+8 piercing"
  - name: "Melee strike"
    desc: "Dagger +20 (`pf2:1`) (agile, deadly d6, finesse, magical, thrown 20, versatile s), **Damage** 2d4+8 piercing"
  - name: "Melee strike"
    desc: "Sword Cane +20 (`pf2:1`) (agile, concealable, finesse, magical), **Damage** 2d8+8 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Accuser agents might be high court advocates, official spymasters, or innocuous adjutants delivering important messages to magistrates, generals, officers, or mercenaries. They have ample latitude in matters of government security, though they sometimes have little oversight. When their findings demand an official response, accuser agents present cases before national tribunals or in royal courts.

Larger societies rely on those with the authority and the ability to interpret and enforce laws. Some carry out these duties fairly, but others are harsh and cruel, imposing severe punishments on anyone unable to pay for clemency.

```statblock
creature: "Accuser Agent"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
