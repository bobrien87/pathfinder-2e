---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Deluded Mob"
level: "4"
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
    desc: "+7"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +12, Intimidation +9, Conspiracy Lore +6"
abilityMods: ["+6", "+1", "+4", "+0", "-1", "+1"]
abilities_top:
  - name: "Irrational"
    desc: "The deluded mob is severely disconnected from reality. Diplomacy checks to [[Make an Impression]] or otherwise sway their worldview automatically fail."
  - name: "Surrounded"
    desc: "When they feel cornered, the mob lashes out more recklessly. While the deluded mob is flanked, Flail Desperately and Throw Detritus are DC 17 and deal an additional 2 damage per action spent on the activity."
armorclass:
  - name: AC
    desc: "19; **Fort** +12, **Ref** +9, **Will** +7"
health:
  - name: HP
    desc: "75; **Weaknesses** area damage 5, splash damage 5"
abilities_mid:
  - name: "Troop Defenses"
    desc: "**Thresholds** 50 (3 segments), 25 (2 segments) <br>  <br> Troops are composed of many individuals, represented by four \"segments\" on a battle grid. Each segment is 10 feet on each side and as tall as the individual members of the troop. Segments must remain contiguous. Each one has to share at least 5 feet of one of its edges with another segment—being adjacent on a diagonal isn't sufficient! You can measure flanking, cover, and the like using the center of any segment. <br>  <br> A troop has two Hit Point thresholds in its HP entry and loses segments as it crosses thresholds. Typically, the higher threshold is at 2/3 of the troop's maximum Hit Points and the lower is at 1/3 of its maximum. Once the troop drops below the higher threshold, it loses one segment, leaving three segments (12 squares) remaining and setting the first threshold as the troop's new maximum Hit Points. This repeats when the troop drops below the lower threshold, leaving two segments (8 squares). At 0 Hit Points, the troop disperses entirely, with the few remaining members surrendering, [[Fleeing]], or easily dispatched, as determined by the GM. Typically the creature who caused the troop to lose a segment decides which to remove, or the GM decides when a specific creature wasn't responsible. To restore lost segments and maximum Hit Points, a troop needs to spend downtime to use long-term treatment on casualties or recruit new members to replace the fallen. <br>  <br> Troops are typically immune to non-damaging effects that target a single creature, such as a [[Charm]] spell or the [[Demoralize]] action. An ability that can target 5 or more creatures can target an entire segment, increasing to two segments if it can target 10 or more creatures and to the entire troop if it can target 20 or more creatures. An ability that affects all creatures in a certain range affects all segments in range (make any checks or saves separately for each segment). As examples, an 8th rank *charm* spell (with 10 targets) can affect two segments, and an ability that Demoralizes all creatures within 30 feet of you would affect all segments that are fully within that range. A non-damaging ability that would prevent a segment from acting, cause them to flee, or otherwise make them unable to function as part of the troop for a round or more removes the segment entirely. The troop loses a number of HP required to bring it to the next threshold. If an ability both deals damage and has a non-damaging effect, apply the damage then the rest of the effect."
  - name: "Troop Movement"
    desc: "Whenever a troop moves, you move one of its segments and the other segments follow behind it. At the end of the movement, you can group the other segments adjacent to the one you moved as you see fit, provided none of them moves farther than the moving segment. If you choose not to move the troop any distance, you can instead reshape the position of all the segments as long as one stays in place."
  - name: "Victim Complex"
    desc: "As they lose members, the deluded mob takes the opposition against them as proof that they're right, bolstering their resolve. The deluded mob gains a +2 circumstance bonus to Will saves at 50 or fewer Hit Points, or a +4 circumstance bonus at 25 HP or fewer."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Flail Desperately"
    desc: "`pf2:1` `pf2:1` to `pf2:3` <br>  <br> **Frequency** once per round <br>  <br> **Effect** The deluded mob uses their fists, wooden planks, and anything else they can pick up to attack each enemy in a @Template[type:emanation|distance:5] with fervor, if not coordination (DC 18 [[Reflex]] save). The damage depends on the number of actions. <br>  <br> `pf2:1` @Damage[1d8[untyped]|options:area-damage] damage <br>  <br> `pf2:2` @Damage[(1d8+6)[untyped]|options:area-damage,action:cost:2] damage <br>  <br> `pf2:3` @Damage[(2d8+6)[untyped]|options:area-damage,action:cost:3] damage"
  - name: "Throw Detritus"
    desc: "`pf2:2` The deluded mob hurls detritus in a @Template[type:burst|distance:10] within 30 feet that deals @Damage[2d8[bludgeoning]|options:area-damage] damage with a DC 18 [[Reflex]] save. When the mob is reduced to 2 or fewer segments, this area decreases to a @Template[type:burst|distance:5]."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Pulled astray by lies, bribes, and propaganda, these desperate people are convinced to fight on their behalf of utter villains. Conspiracists, propagandists, masterminds, despots, and more take advantage of these mobs.

Villains pursue selfish and cruel goals, trampling over anyone in their way.

```statblock
creature: "Deluded Mob"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
