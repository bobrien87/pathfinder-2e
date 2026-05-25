---
type: creature
group: ["Halfling", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Bill-Band"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Halfling"
trait_02: "Humanoid"
trait_03: "Troop"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10"
languages: "Common, Halfling"
skills:
  - name: Skills
    desc: "Acrobatics +12, Athletics +13, Intimidation +13, Sports Lore +11"
abilityMods: ["+4", "+3", "+4", "+0", "-1", "+2"]
abilities_top:
  - name: "Keen Eyes"
    desc: "The halfling gains a +2 circumstance bonus when using the [[Seek]] action to find [[Hidden]] or [[Undetected]] creatures within 30 feet of them. Whenever the halfling targets a creature that is [[Concealed]] or hidden from them, reduce the DC of the flat check to DC 3 flat check for a concealed target or DC 9 flat check for a hidden one."
  - name: "Overwhelming Scrum"
    desc: "The bill-band swarms in and around other creatures. They can move into other creatures' spaces, and other creatures can move into their spaces. The bill-band's spaces are difficult terrain to other creatures."
armorclass:
  - name: AC
    desc: "20; **Fort** +13, **Ref** +12, **Will** +8"
health:
  - name: HP
    desc: "90; (4 segments); Thresholds 60 (3 segments), 30 (2 segments); **Weaknesses** area damage 5, splash damage 5"
abilities_mid:
  - name: "+3 Status vs. Intimidation Checks"
    desc: ""
  - name: "Troop Defenses"
    desc: "**Thresholds** 60 (3 segments), 30 (2 segments) <br>  <br> Troops are composed of many individuals, represented by four \"segments\" on a battle grid. Each segment is 10 feet on each side and as tall as the individual members of the troop. Segments must remain contiguous. Each one has to share at least 5 feet of one of its edges with another segment—being adjacent on a diagonal isn't sufficient! You can measure flanking, cover, and the like using the center of any segment. <br>  <br> A troop has two Hit Point thresholds in its HP entry and loses segments as it crosses thresholds. Typically, the higher threshold is at 2/3 of the troop's maximum Hit Points and the lower is at 1/3 of its maximum. Once the troop drops below the higher threshold, it loses one segment, leaving three segments (12 squares) remaining and setting the first threshold as the troop's new maximum Hit Points. This repeats when the troop drops below the lower threshold, leaving two segments (8 squares). At 0 Hit Points, the troop disperses entirely, with the few remaining members surrendering, [[Fleeing]], or easily dispatched, as determined by the GM. Typically the creature who caused the troop to lose a segment decides which to remove, or the GM decides when a specific creature wasn't responsible. To restore lost segments and maximum Hit Points, a troop needs to spend downtime to use long-term treatment on casualties or recruit new members to replace the fallen. <br>  <br> Troops are typically immune to non-damaging effects that target a single creature, such as a [[Charm]] spell or the [[Demoralize]] action. An ability that can target 5 or more creatures can target an entire segment, increasing to two segments if it can target 10 or more creatures and to the entire troop if it can target 20 or more creatures. An ability that affects all creatures in a certain range affects all segments in range (make any checks or saves separately for each segment). As examples, an 8th rank *charm* spell (with 10 targets) can affect two segments, and an ability that Demoralizes all creatures within 30 feet of you would affect all segments that are fully within that range. A non-damaging ability that would prevent a segment from acting, cause them to flee, or otherwise make them unable to function as part of the troop for a round or more removes the segment entirely. The troop loses a number of HP required to bring it to the next threshold. If an ability both deals damage and has a non-damaging effect, apply the damage then the rest of the effect."
  - name: "Troop Movement"
    desc: "Whenever a troop moves, you move one of its segments and the other segments follow behind it. At the end of the movement, you can group the other segments adjacent to the one you moved as you see fit, provided none of them moves farther than the moving segment. If you choose not to move the troop any distance, you can instead reshape the position of all the segments as long as one stays in place."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Down to Our Level"
    desc: "`pf2:2` **Frequency** once per round <br>  <br> **Effect** The bill-band deliberately gets under the feet of their opponents, proving they are greater than the sum of their parts. The bill-band attempts to `act trip` all creatures in or adjacent to their space. They roll one Athletics check and compare the result to the Reflex DC of each target."
  - name: "Firecracker Salvo"
    desc: "`pf2:2` **Frequency** once per round <br>  <br> **Effect** The bill-band launches a barrage of lit firecrackers that, upon impact, burst into light and sound. Each creature in a @Template[type:burst|distance:10] within 60 feet takes @Damage[1d12[sonic]|options:area-damage] damage with a DC 19 [[Reflex]] save. A creature that fails its save is also [[Dazzled]] for 1 round. When the bill-band is reduced to 2 or fewer segments, this area decreases to a @Template[type:burst|distance:5]."
  - name: "Stick It to 'Em!"
    desc: "`pf2:1` `pf2:1` to `pf2:3` <br>  <br> **Frequency** once per round <br>  <br> **Effect** The bill-band swings barely coordinated fists and feet at each enemy in their space and in a @Template[type:emanation|distance:5], with a DC 19 [[Reflex]] save. The damage depends on the number of actions. <br>  <br> `pf2:1` @Damage[1d6[bludgeoning]|options:area-damage] damage <br>  <br> `pf2:2` @Damage[(2d6+4)[bludgeoning]|options:area-damage] damage <br>  <br> `pf2:3` @Damage[(3d6+6)[bludgeoning]|options:area-damage] damage"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Boisterous collectives of thrill-seeking halflings join in bill-bands to engage in spirited competitions and lively sports. They foster a sense of camaraderie among their members while leaving a trail of chaos in their wake.

Halflings thrive on simple pleasures—having a pint at the pub or warming their feet by the hearth.

```statblock
creature: "Bill-Band"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
