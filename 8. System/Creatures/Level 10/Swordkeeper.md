---
type: creature
group: ["Construct", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Swordkeeper"
level: "10"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +21, Athletics +23"
abilityMods: ["+7", "+5", "+5", "-5", "+2", "-5"]
abilities_top:
  - name: "Central Weapon"
    desc: "A swordkeeper's torso houses a single weapon of a level no higher than the swordkeeper. While the swordkeeper is operational, the chamber requires four successful DC 32 Thievery checks to [[Disable a Device]] to open; on a critical failure, magical backlash deals 6d6 force damage (DC 30 [[Reflex]] save) to the creature attempting the check. <br>  <br> If the swordkeeper is [[Grabbed]], [[Immobilized]], [[Prone]], or [[Stunned]], both DCs are reduced by 2. <br>  <br> If the weapon is removed, the swordkeeper's echoblades vanish."
armorclass:
  - name: AC
    desc: "29 31 with guard raised; **Fort** +21, **Ref** +19, **Will** +14"
health:
  - name: HP
    desc: "245"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Echoblade +23 (`pf2:1`) (magical, reach 10 ft., versatile p), **Damage** 2d8+13 slashing plus 1d8 force"
  - name: "Melee strike"
    desc: "Echoblade +23 (`pf2:1`) (agile, magical, thrown 30), **Damage** 2d8+13 slashing plus 1d8 force"
  - name: "Melee strike"
    desc: "Fist +23 (`pf2:1`) (agile, reach 10 ft., unarmed), **Damage** 2d8+13 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Colossal Echo"
    desc: "`pf2:2` **Requirements** The swordkeeper has a central weapon <br>  <br> **Effect** The swordkeeper projects a massive echoblade held in all four hands, dealing @Damage[9d8[force]|options:area-damage] damage to all creatures in a @Template[type:line|distance:30] (DC 30 [[Reflex]] save). It can't use Colossal Echo again for 1d4 rounds."
  - name: "Echoblade Flurry"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The swordkeeper makes two melee echoblade Strikes. If both Strikes hit the same creature, combine their damage for the purpose of resistances and weakness. Apply the swordkeeper's multiple attack penalty normally."
  - name: "Project Echoblade"
    desc: "`pf2:0` **Requirements** The swordkeeper has a central weapon <br>  <br> **Effect** The swordkeeper projects an echoblade—a force copy of its central weapon that deals an additional 1d8 force damage and gains thrown 30 feet. Echoblades inherit the weapon damage dice, weapon traits, and runes of the central weapon but no other abilities or activations. The swordkeeper gains access to their critical specialization effects. The swordkeeper can have up to four echoblades at once; unattended echoblades vanish at the end of the swordkeeper's turn."
  - name: "Raise Guard"
    desc: "`pf2:1` **Effect** The swordkeeper raises an echoblade to protect itself, gaining a +2 circumstance bonus to AC until the start of its next turn. <br>  <br> > [!danger] Effect: Raise Guard"
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Collectors who want to guard their magical arsenals procure or build swordkeepers. These multi-armed constructs are equal parts display case and security system, each holding a single weapon within its body and projecting copies of the weapon it stores to deter would-be thieves.

```statblock
creature: "Swordkeeper"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
