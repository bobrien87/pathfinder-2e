---
type: creature
group: ["Beast", "Tane"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Bandersnatch"
level: "17"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Beast"
trait_02: "Tane"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+30; [[Darkvision]], [[Scent]] (precise) 120 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +30, Athletics +33, Intimidation +32, Stealth +32, Survival +28"
abilityMods: ["+9", "+6", "+6", "-4", "+6", "+6"]
abilities_top:
  - name: "Planar Acclimation"
    desc: "The bandersnatch treats the plane it is on as its home plane."
  - name: "Pain"
    desc: "A bandersnatch's quills create exceptionally painful wounds. The wounded creature must succeed at a DC 38 [[Fortitude]] save to resist becoming [[Drained]] 1 ([[Drained]] 2 on a critical failure) by this pain. Further bandersnatch Strikes that cause pain increase the amount of drain by 1 for each failed save to a maximum of drained 4."
  - name: "Relentless Tracker"
    desc: "The bandersnatch can [[Track]] while moving at its full speed."
armorclass:
  - name: AC
    desc: "41; **Fort** +32, **Ref** +30, **Will** +27"
health:
  - name: HP
    desc: "335; fast healing 15; **Immunities** confused"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Fast Healing 15"
    desc: "A monster with this ability regains the given number of Hit Points each round at the beginning of its turn."
  - name: "Confusing Gaze"
    desc: "20 feet. <br>  <br> When a creature ends its turn in the aura, it must succeed at a DC 35 [[Will]] save or become [[Confused]] for 1 round."
  - name: "Quick Recovery"
    desc: "The bandersnatch recovers with frightening speed. At the end of its turn, it reduces the value of one debilitating condition it suffers (with the exception of [[Dying]]) by 1. If it's [[Blinded]], [[Dazzled]], [[Deafened]], [[Fatigued]], [[Fleeing]], or [[Petrified]], it can instead succeed at a DC 16 flat check to end one of these conditions of its choice; it can't use quick recovery on other conditions that lack values."
  - name: "Reactive Strike (Tail Only)"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +34 (`pf2:1`) (magical, reach 15 ft., unarmed), **Damage** 3d12+19 piercing"
  - name: "Melee strike"
    desc: "Claws +34 (`pf2:1`) (agile, magical, reach 15 ft.), **Damage** 3d8+19 slashing"
  - name: "Melee strike"
    desc: "Tail +34 (`pf2:1`) (fatal d8, magical, reach 20 ft.), **Damage** 3d4+19 piercing plus [[Pain]]"
  - name: "Ranged strike"
    desc: "Quill +30 (`pf2:1`) (range 100 ft.), **Damage** 3d4+19 piercing plus [[Pain]]"
spellcasting: []
abilities_bot:
  - name: "Focus Gaze"
    desc: "`pf2:1` The bandersnatch fixes its gaze at a creature it can see within 20 feet. The target must immediately attempt a Will save against the bandersnatch's Confusing Gaze. After attempting the save, the creature is temporarily immune to a bandersnatch's Confusing Gaze until the start of the bandersnatch's next turn."
  - name: "Frumious Charge"
    desc: "`pf2:2` The bandersnatch Strides, ignoring difficult terrain, then makes two claw Strikes at the end of its movement."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Bandersnatches are great six-legged cats with wicked quills running down the length of their bodies down to the tips of their mighty tails. As with other legendary creatures from the First World, such as the jabberwock, bandersnatches belong to the infamous group of creatures known collectively as the "Tane." These terrifying hunters take great delight in taking down other deadly or intelligent predators by perfectly adapting to any environment they find themselves in. A bandersnatch stalks their quarry before lashing out with speed and ferocity. Those who survive a bandersnatch attack will confirm that while the cats' fangs and claws are deadly, their eyes are their greatest weapon of all. A bandersnatch's eyes are constantly shifting in color, intensity, and design, causing those they gaze upon to fall into a confused panic.

```statblock
creature: "Bandersnatch"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
