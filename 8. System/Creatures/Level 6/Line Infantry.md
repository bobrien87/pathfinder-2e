---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Line Infantry"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Troop"
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
    desc: "Athletics +15, Warfare Lore +12"
abilityMods: ["+5", "+2", "+3", "+0", "+1", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "24; **Fort** +15, **Ref** +14, **Will** +13"
health:
  - name: HP
    desc: "96; **Weaknesses** area damage 5, splash damage 5"
abilities_mid:
  - name: "No Retreat"
    desc: "These soldiers have been extensively trained to hold their ground no matter the situation. If any effect would force the line infantry to move, reduce the distance by 5 feet. Any time they would be affected by the [[Fleeing]] condition, the line infantry is instead [[Slowed]] 2 for the same duration."
  - name: "Troop Defenses"
    desc: "**Thresholds** 64 (3 segments), 32 (2 segments) <br>  <br> Troops are composed of many individuals, represented by four \"segments\" on a battle grid. Each segment is 10 feet on each side and as tall as the individual members of the troop. Segments must remain contiguous. Each one has to share at least 5 feet of one of its edges with another segment—being adjacent on a diagonal isn't sufficient! You can measure flanking, cover, and the like using the center of any segment. <br>  <br> A troop has two Hit Point thresholds in its HP entry and loses segments as it crosses thresholds. Typically, the higher threshold is at 2/3 of the troop's maximum Hit Points and the lower is at 1/3 of its maximum. Once the troop drops below the higher threshold, it loses one segment, leaving three segments (12 squares) remaining and setting the first threshold as the troop's new maximum Hit Points. This repeats when the troop drops below the lower threshold, leaving two segments (8 squares). At 0 Hit Points, the troop disperses entirely, with the few remaining members surrendering, [[Fleeing]], or easily dispatched, as determined by the GM. Typically the creature who caused the troop to lose a segment decides which to remove, or the GM decides when a specific creature wasn't responsible. To restore lost segments and maximum Hit Points, a troop needs to spend downtime to use long-term treatment on casualties or recruit new members to replace the fallen. <br>  <br> Troops are typically immune to non-damaging effects that target a single creature, such as a [[Charm]] spell or the [[Demoralize]] action. An ability that can target 5 or more creatures can target an entire segment, increasing to two segments if it can target 10 or more creatures and to the entire troop if it can target 20 or more creatures. An ability that affects all creatures in a certain range affects all segments in range (make any checks or saves separately for each segment). As examples, an 8th rank *charm* spell (with 10 targets) can affect two segments, and an ability that Demoralizes all creatures within 30 feet of you would affect all segments that are fully within that range. A non-damaging ability that would prevent a segment from acting, cause them to flee, or otherwise make them unable to function as part of the troop for a round or more removes the segment entirely. The troop loses a number of HP required to bring it to the next threshold. If an ability both deals damage and has a non-damaging effect, apply the damage then the rest of the effect."
  - name: "Troop Movement"
    desc: "Whenever a troop moves, you move one of its segments and the other segments follow behind it. At the end of the movement, you can group the other segments adjacent to the one you moved as you see fit, provided none of them moves farther than the moving segment. If you choose not to move the troop any distance, you can instead reshape the position of all the segments as long as one stays in place."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Bolt Salvo"
    desc: "`pf2:3` The line infantry draws, loads, and shoots a salvo from their crossbows. The salvo is a @Template[type:burst|distance:10] within 120 feet that deals @Damage[2d8[piercing]|options:area-damage] damage (DC 21 [[Reflex]] save). When the line infantry is reduced to 2 or fewer segments, this area decreases to a @Template[type:burst|distance:5]."
  - name: "Clash of Steel"
    desc: "`pf2:1` `pf2:1` to `pf2:3` <br>  <br> **Frequency** once per round <br>  <br> **Effect** The line infantry lays into each enemy in a @Template[type:emanation|distance:5], with a DC 21 [[Reflex]] save. The damage depends on the number of actions. <br>  <br> `pf2:1` @Damage[(1d6+2)[slashing]|options:area-damage] damage <br>  <br> `pf2:2` @Damage[(2d6+7)[slashing]|options:area-damage] damage <br>  <br> `pf2:3` @Damage[(3d6+10)[slashing]|options:area-damage] damage"
  - name: "Drilled in Formations"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The line infantry uses [[Change Formation]]. A line infantry unit typically knows the marching column and wedge formations."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Infantry are the backbone of most armies. These professional soldiers, marked by matching uniforms, straightforward tactics, and the drive to follow well-practiced orders, make up the bulk of most military forces—but are often considered the most expendable.

A military serves to defend and fight on behalf of nations and can be trained and deployed in various ways.

```statblock
creature: "Line Infantry"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
