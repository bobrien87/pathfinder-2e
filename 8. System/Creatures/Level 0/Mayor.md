---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mayor"
level: "0"
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
    desc: "+9"
languages: "Common (up to 2 additional languages spoken in their settlement)"
skills:
  - name: Skills
    desc: "Deception +15, Diplomacy +15, Intimidation +15, Society +13, Guild Lore +11"
abilityMods: ["+0", "+2", "+1", "+1", "+2", "+3"]
abilities_top:
  - name: "Political Specialist"
    desc: "For encounters involving seeking political favors, the mayor is a 6th-level challenge."
  - name: "Pulse of the Electorate"
    desc: "The mayor can quickly find things out, and 1 hour after anyone in their settlement becomes aware of an event or activity, the mayor becomes aware of it, so long as they have had time to hobnob with their constituents."
armorclass:
  - name: AC
    desc: "14; **Fort** +6, **Ref** +3, **Will** +14"
health:
  - name: HP
    desc: "16"
abilities_mid:
  - name: "But Will It Lose Me Votes"
    desc: "`pf2:r` **Frequency** once per hour <br>  <br> **Trigger** A creature succeeds (but doesn't critically succeed) at a Diplomacy check to make a [[Request]] of the mayor <br>  <br> **Effect** The triggering creature (or one of its allies) must attempt the check again within the next hour, this time against the mayor's Society DC. Society or a relevant Lore skill may be used for this check instead of Diplomacy."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Decorative Sword of Station +6 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d6 piercing"
  - name: "Melee strike"
    desc: "Fist +6 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The mayor is the political leader of a settlement. While not always an elected position, it usually involves devoting time to both civic and ceremonial functions and knowing the needs of their settlement.

Larger societies rely on those with the authority and the ability to interpret and enforce laws. Some carry out these duties fairly, but others are harsh and cruel, imposing severe punishments on anyone unable to pay for clemency.

```statblock
creature: "Mayor"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
