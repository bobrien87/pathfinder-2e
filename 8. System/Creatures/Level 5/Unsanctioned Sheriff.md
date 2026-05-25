---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Unsanctioned Sheriff"
level: "5"
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
    desc: "+13"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +13, Deception +11, Diplomacy +11, Intimidation +13, Society +13"
abilityMods: ["+4", "+2", "+2", "+0", "+2", "+2"]
abilities_top:
  - name: "Greased Palms"
    desc: "Money talks, and no one knows that better than the unsanctioned sheriff. A creature that pays the sheriff at least 5 gp gains a +2 status bonus to [[Gather Information]] in the sheriff's settlement for the next 24 hours. <br>  <br> > [!danger] Effect: Greased Palms"
armorclass:
  - name: AC
    desc: "22; **Fort** +11, **Ref** +11, **Will** +13"
health:
  - name: HP
    desc: "75"
abilities_mid:
  - name: "+2 to Sense Motive"
    desc: ""
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Sap +15 (`pf2:1`) (agile, nonlethal), **Damage** 1d6+7 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +15 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+7 bludgeoning"
  - name: "Ranged strike"
    desc: "Dueling Pistol +13 (`pf2:1`) (concealable, concussive, fatal d10, reload 1, range 60 ft.), **Damage** 1d6+5 piercing"
spellcasting: []
abilities_bot:
  - name: "Lay Down the Law"
    desc: "`pf2:1` **Requirements** The sheriff's last action this turn was a successful Strike against a creature within 30 feet <br>  <br> **Effect** The sheriff yells a command at the creature they hit. The target must succeed at a DC 22 [[Will]] save or spend the first action on its next turn doing as commanded (or all its actions on its next turn on a critical failure). The sheriff can command a creature to approach the sheriff, release what its holding, or drop [[Prone]]. Regardless of the result of its save, the creature is temporarily immune for 10 minutes."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Believing the ends justify the means, the unsanctioned sheriff is unafraid to use others for their own gain, through bribes, manipulation, or force.

These lone wolves have an aura of mystery, bravado, and swagger.

```statblock
creature: "Unsanctioned Sheriff"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
