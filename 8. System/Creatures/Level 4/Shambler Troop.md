---
type: creature
group: ["Mindless", "Troop"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Shambler Troop"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Mindless"
trait_02: "Troop"
trait_03: "Undead"
trait_04: "Unholy"
trait_05: "Zombie"
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: ""
abilityMods: ["+5", "+0", "+3", "-5", "+1", "-2"]
abilities_top:
  - name: "Slow"
    desc: "A shambler troop is permanently [[Slowed]] 1 and can't use reactions."
  - name: "Grave Tide"
    desc: "The shambler troop is less organized than most troops. It can move into other creatures' spaces, and other creatures can move into its spaces. Its spaces are difficult terrain to other creatures."
armorclass:
  - name: AC
    desc: "18; **Fort** +11, **Ref** +8, **Will** +9"
health:
  - name: HP
    desc: "90; void healing; Thresholds 60 (3 segments), 30 (2 segments); **Immunities** bleed, death effects, disease, mental, paralyzed, poison, unconscious; **Weaknesses** area damage 5, slashing 5, splash damage 5, vitality 5"
abilities_mid:
  - name: "Troop Defenses"
    desc: "**Thresholds** 60 (3 segments), 30 (2 segments) <br>  <br> Troops are composed of many individuals, represented by four \"segments\" on a battle grid. Each segment is 10 feet on each side and as tall as the individual members of the troop. Segments must remain contiguous. Each one has to share at least 5 feet of one of its edges with another segment—being adjacent on a diagonal isn't sufficient! You can measure flanking, cover, and the like using the center of any segment. <br>  <br> A troop has two Hit Point thresholds in its HP entry and loses segments as it crosses thresholds. Typically, the higher threshold is at 2/3 of the troop's maximum Hit Points and the lower is at 1/3 of its maximum. Once the troop drops below the higher threshold, it loses one segment, leaving three segments (12 squares) remaining and setting the first threshold as the troop's new maximum Hit Points. This repeats when the troop drops below the lower threshold, leaving two segments (8 squares). At 0 Hit Points, the troop disperses entirely, with the few remaining members surrendering, [[Fleeing]], or easily dispatched, as determined by the GM. Typically the creature who caused the troop to lose a segment decides which to remove, or the GM decides when a specific creature wasn't responsible. To restore lost segments and maximum Hit Points, a troop needs to spend downtime to use long-term treatment on casualties or recruit new members to replace the fallen. <br>  <br> Troops are typically immune to non-damaging effects that target a single creature, such as a [[Charm]] spell or the [[Demoralize]] action. An ability that can target 5 or more creatures can target an entire segment, increasing to two segments if it can target 10 or more creatures and to the entire troop if it can target 20 or more creatures. An ability that affects all creatures in a certain range affects all segments in range (make any checks or saves separately for each segment). As examples, an 8th rank *charm* spell (with 10 targets) can affect two segments, and an ability that Demoralizes all creatures within 30 feet of you would affect all segments that are fully within that range. A non-damaging ability that would prevent a segment from acting, cause them to flee, or otherwise make them unable to function as part of the troop for a round or more removes the segment entirely. The troop loses a number of HP required to bring it to the next threshold. If an ability both deals damage and has a non-damaging effect, apply the damage then the rest of the effect."
  - name: "Troop Movement"
    desc: "Whenever a troop moves, you move one of its segments and the other segments follow behind it. At the end of the movement, you can group the other segments adjacent to the one you moved as you see fit, provided none of them moves farther than the moving segment. If you choose not to move the troop any distance, you can instead reshape the position of all the segments as long as one stays in place."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Shambling Onslaught"
    desc: "`pf2:1` `pf2:1` to `pf2:2` <br>  <br> **Frequency** once per round <br>  <br> **Effect** The shamblers lash out at any enemies in their squares or within a @Template[type:emanation|distance:5] (DC 18 [[Reflex]] save). The damage depends on the number of actions. <br>  <br> `pf2:1` @Damage[(2d6+5)[bludgeoning]|options:area-damage] damage <br>  <br> `pf2:2` @Damage[(2d6+9)[bludgeoning]|options:area-damage] damage"
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

This shuffling mass of decaying flesh moves with dull but singular focus.

Necromancers most often create these mindless undead as obedient, expendable servitors. Left to its own devices, a zombie seeks only to consume the living, stopping only when its rotting body can no longer hold together.

```statblock
creature: "Shambler Troop"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
