---
type: creature
group: ["Hobgoblin", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hobgoblin Battalion"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Hobgoblin"
trait_02: "Humanoid"
trait_03: "Troop"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Darkvision]]"
languages: "Common, Goblin"
skills:
  - name: Skills
    desc: "Athletics +15, Intimidation +14, Warfare Lore +12"
abilityMods: ["+5", "+0", "+3", "+0", "+2", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "23; **Fort** +15, **Ref** +12, **Will** +14"
health:
  - name: HP
    desc: "90; Thresholds 60 (3 segments), 30 (2 segments); **Weaknesses** area damage 8, splash damage 8"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Troop Defenses"
    desc: "**Thresholds** 60 (3 segments), 30 (2 segments) <br>  <br> Troops are composed of many individuals, represented by four \"segments\" on a battle grid. Each segment is 10 feet on each side and as tall as the individual members of the troop. Segments must remain contiguous. Each one has to share at least 5 feet of one of its edges with another segment—being adjacent on a diagonal isn't sufficient! You can measure flanking, cover, and the like using the center of any segment. <br>  <br> A troop has two Hit Point thresholds in its HP entry and loses segments as it crosses thresholds. Typically, the higher threshold is at 2/3 of the troop's maximum Hit Points and the lower is at 1/3 of its maximum. Once the troop drops below the higher threshold, it loses one segment, leaving three segments (12 squares) remaining and setting the first threshold as the troop's new maximum Hit Points. This repeats when the troop drops below the lower threshold, leaving two segments (8 squares). At 0 Hit Points, the troop disperses entirely, with the few remaining members surrendering, [[Fleeing]], or easily dispatched, as determined by the GM. Typically the creature who caused the troop to lose a segment decides which to remove, or the GM decides when a specific creature wasn't responsible. To restore lost segments and maximum Hit Points, a troop needs to spend downtime to use long-term treatment on casualties or recruit new members to replace the fallen. <br>  <br> Troops are typically immune to non-damaging effects that target a single creature, such as a [[Charm]] spell or the [[Demoralize]] action. An ability that can target 5 or more creatures can target an entire segment, increasing to two segments if it can target 10 or more creatures and to the entire troop if it can target 20 or more creatures. An ability that affects all creatures in a certain range affects all segments in range (make any checks or saves separately for each segment). As examples, an 8th rank *charm* spell (with 10 targets) can affect two segments, and an ability that Demoralizes all creatures within 30 feet of you would affect all segments that are fully within that range. A non-damaging ability that would prevent a segment from acting, cause them to flee, or otherwise make them unable to function as part of the troop for a round or more removes the segment entirely. The troop loses a number of HP required to bring it to the next threshold. If an ability both deals damage and has a non-damaging effect, apply the damage then the rest of the effect."
  - name: "Troop Movement"
    desc: "Whenever a troop moves, you move one of its segments and the other segments follow behind it. At the end of the movement, you can group the other segments adjacent to the one you moved as you see fit, provided none of them moves farther than the moving segment. If you choose not to move the troop any distance, you can instead reshape the position of all the segments as long as one stays in place."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Coordinated Strikes"
    desc: "`pf2:1` `pf2:1` to `pf2:3` <br>  <br> **Frequency** once per round <br>  <br> **Effect** The battalion thrusts their spears at each enemy in a @Template[type:emanation|distance:5] with a DC 21 [[Reflex]] save. The damage depends on the number of actions. <br>  <br> `pf2:1` @Damage[(1d6+2)[slashing]|options:area-damage] damage <br>  <br> `pf2:2` @Damage[(2d6+5)[slashing]|options:area-damage] damage <br>  <br> `pf2:3` @Damage[(3d12+7)[slashing]|options:area-damage] damage"
  - name: "Focused Volley"
    desc: "`pf2:2` The hobgoblin battalion's archers draw or reload their crossbows, then launch a ranged attack in the form of a volley. This volley is a @Template[type:burst|distance:10] within 120 feet that deals @Damage[2d8[piercing]|options:area-damage] damage with a DC 21 [[Reflex]] save. When the hobgoblin battalion is reduced to 2 or fewer segments, this area is reduced to a @Template[type:burst|distance:5]."
  - name: "Perfect Formation"
    desc: "`pf2:1` The battalion raises a perfect guard against explosions. It gains a +2 item bonus to AC and a +2 status bonus to Reflex saves until the start of its next turn."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A hobgoblin battalion is usually composed of multiple soldiers and archers commanded by a single captain, although every battalion also has its own internal hierarchy that clearly defines the chain of command should the current captain fall in battle.

Hobgoblins are respected across Golarion for their unmatched expertise in the art of war. The recent foundation of the hobgoblin nation of Oprak and its unprecedented acts of diplomacy, including non-aggression pacts with the neighboring nations of Nidal and Nirmathas, has given some hope that a lasting peace might finally be established; however, there remains no shortage of unaffiliated hobgoblin raiders and pillagers.

```statblock
creature: "Hobgoblin Battalion"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
