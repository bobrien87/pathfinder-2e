---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Flamboyant Thief"
level: "15"
rare_01: "Rare"
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
    desc: "+27"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +29, Athletics +26, Deception +28, Intimidation +26, Performance +28, Society +24, Stealth +31, Thievery +31, Underworld Lore +28"
abilityMods: ["+5", "+6", "+1", "+3", "+4", "+5"]
abilities_top:
  - name: "Flamboyant Performance"
    desc: "A flamboyant thief's attempts to [[Steal]] don't automatically fail even if a creature is in combat or on guard. While being observed, the thief gains a +2 circumstance bonus to Deception checks to [[Create a Diversion]] or `act feint` and to Thievery checks to `act palm-an-object` or `act steal`. However, they are compelled to leave a tangible sign of their presence, such as a calling card or symbol—often in place of a stolen item."
  - name: "Vanishing Act"
    desc: "The flamboyant thief can `act hide` and `act sneak` even without having cover or being [[Concealed]]."
  - name: "Spectacular Attack"
    desc: "All the flamboyant thief's Strikes deal an additional 3d6 precision damage or 6d6 if the target is [[Fascinated]] with the thief. After the thief Strikes a creature, that creature becomes fascinated with the thief until the end of the thief's next turn."
armorclass:
  - name: AC
    desc: "37; **Fort** +23, **Ref** +30, **Will** +26"
health:
  - name: HP
    desc: "225"
abilities_mid:
  - name: "Dramatic Entrance"
    desc: "`pf2:0` **Trigger** The flamboyant thief rolls initiative <br>  <br> **Effect** The flamboyant thief draws all eyes to them. They attempt a Performance check, comparing the result against the Will DC of any number of creatures within 120 feet. Each creature the thief succeeds against is [[Fascinated]] with the thief until the end of the thief's next turn."
  - name: "I Say When I'm Here"
    desc: "When any detection, revelation, or scrying magic would reveal the flamboyant thief, the thief becomes aware of it and can attempt to counteract the magic with a counteract rank of 8th level and using their Stealth as their counteract modifier."
  - name: "Nimble Dodge"
    desc: "`pf2:r` **Trigger** The flamboyant thief is targeted with a melee or ranged attack by an attacker it can see. <br>  <br> **Effect** The flamboyant thief gains a +2 circumstance bonus to AC against the triggering attack."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +29 (`pf2:1`) (agile, finesse, magical, versatile s), **Damage** 2d4+11 piercing plus [[Spectacular Attack]]"
  - name: "Melee strike"
    desc: "Dagger +29 (`pf2:1`) (agile, magical, thrown 10, versatile s), **Damage** 2d4+11 piercing plus [[Spectacular Attack]]"
  - name: "Melee strike"
    desc: "Fist +27 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+11 bludgeoning plus [[Spectacular Attack]]"
spellcasting: []
abilities_bot:
  - name: "Dancing Dagger"
    desc: "`pf2:2` The flamboyant thief can Step, attempt a melee dagger Strike, and attempt a ranged dagger Strike, taking the actions in any order. Both Strikes count toward the thief's multiple attack penalty, but it doesn't increase until after both attacks."
  - name: "Dramatic Exit"
    desc: "`pf2:3` The flamboyant thief throws down their smoke ball, then Hides, then Sneaks up to three times with a +2 circumstance bonus to their Stealth checks."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

There's no honor among thieves, but if there were points for style, these thieves would have 10s across the board. Some would say flamboyant thieves value showcasing their skills rather than successfully stealing an item, but what better way to show that you're the best than with an audience?

In the underbelly of society, the lawless reign supreme.

```statblock
creature: "Flamboyant Thief"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
