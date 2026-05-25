---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Palace Guard"
level: "4"
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
    desc: "+12"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +14, Diplomacy +8, Intimidation +8"
abilityMods: ["+4", "+2", "+3", "+0", "+2", "+0"]
abilities_top:
  - name: "+2 to Perception to Initiative"
    desc: ""
armorclass:
  - name: AC
    desc: "21; **Fort** +12, **Ref** +10, **Will** +10"
health:
  - name: HP
    desc: "60"
abilities_mid:
  - name: "Guard's Parry"
    desc: "`pf2:r` **Trigger** A creature attacks the palace guard's liege, and the liege is within the guard's melee reach <br>  <br> **Effect** The liege gains a +2 circumstance bonus to AC against the triggering attack, and the palace guard gains a +2 circumstance bonus to attack and damage rolls until the end of their next turn. <br>  <br> > [!danger] Effect: Guard's Parry (Guard) <br>  <br> > [!danger] Effect: Guard's Parry (Liege)"
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Halberd +14 (`pf2:1`) (reach 10 ft., versatile s), **Damage** 1d10+7 piercing"
  - name: "Melee strike"
    desc: "Fist +14 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+7 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Crowd Control"
    desc: "`pf2:1` **Requirements** The palace guard's last action was a successful halberd Strike <br>  <br> **Effect** The palace guard attempts to [[Reposition]] the creature they hit using their halberd's reach. This attempt neither applies nor counts toward the guard's multiple attack penalty."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Often the younger offspring of minor nobility or those from long lines of trusted staff, palace guards are in charge of defending the royal family and their inner stronghold. Their days consist of guarding doorways, escorting nobles, and keeping those in their charge as safe as possible.

The denizens of a noble court are the most powerful people in a civilization, primed with wealth, station, and authority above the common people.

```statblock
creature: "Palace Guard"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
