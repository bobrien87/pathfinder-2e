---
type: creature
group: ["Humanoid", "Orc"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Orc Veteran Master"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Orc"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Darkvision]]"
languages: "Common, Orcish"
skills:
  - name: Skills
    desc: "Acrobatics +20, Athletics +23, Diplomacy +15, Intimidation +20, Stealth +20, Warfare Lore +18"
abilityMods: ["+5", "+4", "+3", "+0", "+2", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "30; **Fort** +19, **Ref** +20, **Will** +18"
health:
  - name: HP
    desc: "175"
abilities_mid:
  - name: "Fly Through Battle"
    desc: "The veteran master gains an additional reaction each round that can be used only to make a Reactive Pursuit."
  - name: "Reactive Pursuit"
    desc: "`pf2:r` **Trigger** An enemy within reach attempts to move away <br>  <br> **Effect** The veteran master Strides up to their Speed, following the enemy and keeping it in reach throughout its movement until it stops moving or the master has moved their full Speed."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Bo Staff +24 (`pf2:1`) (magical, parry, reach, trip), **Damage** 2d8+13 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +24 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 2d4+13 bludgeoning"
  - name: "Ranged strike"
    desc: "Composite Longbow +23 (`pf2:1`) (deadly d10, magical, propulsive, reload 0, volley 30, range 100 ft.), **Damage** 2d8+10 piercing"
spellcasting: []
abilities_bot:
  - name: "Reshape the Battle"
    desc: "`pf2:1` The veteran master attempts a bo staff Strike. If it hits a creature of the master's size or smaller, the master can automatically [[Reposition]] it to any space within the bo staff's reach."
  - name: "Staff Swipe"
    desc: "`pf2:2` The veteran master extends their reach to smash multiple creatures with their bo. They attempt a bo staff Strike against each enemy in a @Template[type:cone|distance:15]. This counts as two attacks toward their multiple attack penalty, but the penalty doesn't increase until after all the attacks."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

While the sword and shield are reliable and proven in battle, the veteran master is the weapon. They have been hardened by decades of fighting, but they still manage to find peace within themselves to gain a physical advantage.

Orcs have a strict moral code encompassing valor and accomplishment, and they cast out those unwilling to follow it. For the last few generations, orcs have been trying to erase the narratives around their culture as being solely focused on war and violence. They invite other races and adventuring parties inside their holds so they may experience the truth of who the orcs are.

```statblock
creature: "Orc Veteran Master"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
