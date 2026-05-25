---
type: creature
group: ["Leshy", "Plant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Corn Leshy Throng"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Leshy"
trait_02: "Plant"
trait_03: "Troop"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Low-Light Vision]]"
languages: "Common, Fey (speak with plants (corn only))"
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +10, Nature +12"
abilityMods: ["+2", "+3", "+2", "+0", "+2", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "21; **Fort** +8, **Ref** +13, **Will** +10"
health:
  - name: HP
    desc: "54; (4 segments); Thresholds 36 (3 segments), 18 (2 segments); **Weaknesses** area damage 5, splash damage 5"
abilities_mid:
  - name: "Encircling Maze"
    desc: "A corn leshy throng is arranged in rows of stalks to envelop foes, stretching upward to block their vision. It can move into other creatures' spaces, and other creatures can move into its squares. <br>  <br> When a Medium or smaller creature attempts to enter any of the corn leshy throng's spaces, it must attempt a DC 20 [[Survival]] check. If the creature fails, it gets turned around—all the throng's squares are greater difficult terrain for it until the end of this turn. A creature needs to attempt this check only the first time in a round it attempts to enter one of the throng's squares."
  - name: "Troop Defenses"
    desc: "**Thresholds** 36 (3 segments), 18 (2 segments) <br>  <br> Troops are composed of many individuals, represented by four \"segments\" on a battle grid. Each segment is 10 feet on each side and as tall as the individual members of the troop. Segments must remain contiguous. Each one has to share at least 5 feet of one of its edges with another segment—being adjacent on a diagonal isn't sufficient! You can measure flanking, cover, and the like using the center of any segment. <br>  <br> A troop has two Hit Point thresholds in its HP entry and loses segments as it crosses thresholds. Typically, the higher threshold is at 2/3 of the troop's maximum Hit Points and the lower is at 1/3 of its maximum. Once the troop drops below the higher threshold, it loses one segment, leaving three segments (12 squares) remaining and setting the first threshold as the troop's new maximum Hit Points. This repeats when the troop drops below the lower threshold, leaving two segments (8 squares). At 0 Hit Points, the troop disperses entirely, with the few remaining members surrendering, [[Fleeing]], or easily dispatched, as determined by the GM. Typically the creature who caused the troop to lose a segment decides which to remove, or the GM decides when a specific creature wasn't responsible. To restore lost segments and maximum Hit Points, a troop needs to spend downtime to use long-term treatment on casualties or recruit new members to replace the fallen. <br>  <br> Troops are typically immune to non-damaging effects that target a single creature, such as a [[Charm]] spell or the [[Demoralize]] action. An ability that can target 5 or more creatures can target an entire segment, increasing to two segments if it can target 10 or more creatures and to the entire troop if it can target 20 or more creatures. An ability that affects all creatures in a certain range affects all segments in range (make any checks or saves separately for each segment). As examples, an 8th rank *charm* spell (with 10 targets) can affect two segments, and an ability that Demoralizes all creatures within 30 feet of you would affect all segments that are fully within that range. A non-damaging ability that would prevent a segment from acting, cause them to flee, or otherwise make them unable to function as part of the troop for a round or more removes the segment entirely. The troop loses a number of HP required to bring it to the next threshold. If an ability both deals damage and has a non-damaging effect, apply the damage then the rest of the effect."
  - name: "Troop Movement"
    desc: "Whenever a troop moves, you move one of its segments and the other segments follow behind it. At the end of the movement, you can group the other segments adjacent to the one you moved as you see fit, provided none of them moves farther than the moving segment. If you choose not to move the troop any distance, you can instead reshape the position of all the segments as long as one stays in place."
  - name: "Verdant Burst"
    desc: "When the corn leshy throng dies, a burst of primal energy explodes from their body, restoring @Damage[3d8[healing,vitality]|shortLabel] Hit Points to each plant creature in a @Template[type:emanation|distance:30]. This area immediately fills with stalks of corn, becoming difficult terrain. If the terrain is not a viable environment for these plants, they wither after 24 hours."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Boxing Ears"
    desc: "`pf2:1` `pf2:1` to `pf2:3` <br>  <br> **Frequency** once per round <br>  <br> **Effect** The corn leshy throng lashes out with hardened ears of corn to attack each enemy in its space and in a @Template[type:emanation|distance:5], with a DC 18 [[Reflex]] save. The damage depends on the number of actions. <br>  <br> `pf2:1` @Damage[1d6[bludgeoning]|options:area-damage] damage <br>  <br> `pf2:2` @Damage[(2d6+4)[bludgeoning]|options:area-damage] damage <br>  <br> `pf2:3` @Damage[(2d6+8)[bludgeoning]|options:area-damage] damage"
  - name: "Kernel Barrage"
    desc: "`pf2:2` The throng's members fling a bombardment of corn kernels. Each creature in a @Template[type:cone|distance:30] takes @Damage[2d6[bludgeoning]|options:area-damage] damage with a DC 18 [[Reflex]] save. When the throng is reduced to 2 or fewer segments, this area decreases to a @Template[type:cone|distance:15]."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A thick forest or flourishing farm sometimes sees an explosion of primal magic leading to the creation of a multitude of leshies. When still young, these spirits might band together with their crop-mates for protection or to achieve a mutual goal. Used to growing in rows, many corn leshies can form a sizable legion.

Nature spirits inhabit bodies made of plants or fungi, blooming from primal magic to become the small people called leshies. They come in a truly immense number of diverse shapes and sizes, more so than most peoples of Golarion. This variety of forms means a leshy could have a place in nearly any type of setting for any type of story.

```statblock
creature: "Corn Leshy Throng"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
