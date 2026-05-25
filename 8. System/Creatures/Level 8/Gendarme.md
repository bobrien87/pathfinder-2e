---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gendarme"
level: "8"
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
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +18, Intimidation +16, Legal Lore +14"
abilityMods: ["+4", "+1", "+4", "+0", "+3", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "26; **Fort** +19, **Ref** +14, **Will** +17"
health:
  - name: HP
    desc: "120"
abilities_mid:
  - name: "Nerves of Steel"
    desc: "When the gendarme succeeds against a fear effect, they get a critical success instead."
  - name: "Reactive Strike"
    desc: "`pf2:r` The gendarme can `act disarm` instead of Striking. <br>  <br> **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Flail +19 (`pf2:1`) (disarm, magical, sweep, trip), **Damage** 2d6+10 bludgeoning plus [[Improved Knockdown]]"
  - name: "Melee strike"
    desc: "Gauntlet +19 (`pf2:1`) (agile, free hand, magical), **Damage** 1d4+10 bludgeoning plus [[Improved Grab]]"
  - name: "Ranged strike"
    desc: "Composite Longbow +16 (`pf2:1`) (deadly d10, magical, propulsive, reload 0, volley 30, range 100 ft.), **Damage** 1d8+8 piercing"
spellcasting: []
abilities_bot:
  - name: "Shoot Down"
    desc: "`pf2:2` The gendarme carefully makes a ranged Strike. If the Strike deals damage, the target must succeed at a DC 26 [[Reflex]] save saving throw or fall [[Prone]]."
  - name: "Stop in the Name of the Law!"
    desc: "`pf2:2` The gendarme Strides twice and then Demoralizes. On a success, the target is [[Slowed]] with a value equal to its [[Frightened]] value until it is no longer frightened."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Powerful governments retain gendarmes to guard important magistrates, enforce laws protecting national security, reinstate order amid unrest, and capture unusually dangerous criminals. They're also sent to deal with important cases in rural areas without substantial guards of their own.

Larger societies rely on those with the authority and the ability to interpret and enforce laws. Some carry out these duties fairly, but others are harsh and cruel, imposing severe punishments on anyone unable to pay for clemency.

```statblock
creature: "Gendarme"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
