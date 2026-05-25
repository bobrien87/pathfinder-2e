---
type: creature
group: ["Goblin", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Goblin Get Gang"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Goblin"
trait_02: "Humanoid"
trait_03: "Troop"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Darkvision]]"
languages: "Common, Goblin"
skills:
  - name: Skills
    desc: "Athletics +12, Intimidation +13, Performance +13, Stealth +10"
abilityMods: ["+3", "+2", "+3", "+0", "-1", "+4"]
abilities_top:
  - name: "Goblins Bound and Goblins Swing!"
    desc: "Goblins have difficulty staying in formation, especially during combat. The goblin get gang can take a move action only if it has used at least one action to Goblins Slash and Goblins Scar! this turn or if there are no conscious enemies adjacent to it."
armorclass:
  - name: AC
    desc: "21; **Fort** +13, **Ref** +14, **Will** +9"
health:
  - name: HP
    desc: "90; (4 segments); Thresholds 60 (3 segments), 30 (2 segments); **Weaknesses** area damage 5, splash damage 5"
abilities_mid:
  - name: "Goblins Chant and Goblins Sing!"
    desc: "30 feet. The goblin get gang's disharmonious chorus of disturbing lyrics makes it difficult to concentrate. Any creature performing a concentrate action in the area must succeed at a DC 19 [[Will]] save or the action is lost. On a critical success, the creature is temporarily immune for 1 minute."
  - name: "Troop Defenses"
    desc: "**Thresholds** 60 (3 segments), 30 (2 segments) <br>  <br> Troops are composed of many individuals, represented by four \"segments\" on a battle grid. Each segment is 10 feet on each side and as tall as the individual members of the troop. Segments must remain contiguous. Each one has to share at least 5 feet of one of its edges with another segment—being adjacent on a diagonal isn't sufficient! You can measure flanking, cover, and the like using the center of any segment. <br>  <br> A troop has two Hit Point thresholds in its HP entry and loses segments as it crosses thresholds. Typically, the higher threshold is at 2/3 of the troop's maximum Hit Points and the lower is at 1/3 of its maximum. Once the troop drops below the higher threshold, it loses one segment, leaving three segments (12 squares) remaining and setting the first threshold as the troop's new maximum Hit Points. This repeats when the troop drops below the lower threshold, leaving two segments (8 squares). At 0 Hit Points, the troop disperses entirely, with the few remaining members surrendering, [[Fleeing]], or easily dispatched, as determined by the GM. Typically the creature who caused the troop to lose a segment decides which to remove, or the GM decides when a specific creature wasn't responsible. To restore lost segments and maximum Hit Points, a troop needs to spend downtime to use long-term treatment on casualties or recruit new members to replace the fallen. <br>  <br> Troops are typically immune to non-damaging effects that target a single creature, such as a [[Charm]] spell or the [[Demoralize]] action. An ability that can target 5 or more creatures can target an entire segment, increasing to two segments if it can target 10 or more creatures and to the entire troop if it can target 20 or more creatures. An ability that affects all creatures in a certain range affects all segments in range (make any checks or saves separately for each segment). As examples, an 8th rank *charm* spell (with 10 targets) can affect two segments, and an ability that Demoralizes all creatures within 30 feet of you would affect all segments that are fully within that range. A non-damaging ability that would prevent a segment from acting, cause them to flee, or otherwise make them unable to function as part of the troop for a round or more removes the segment entirely. The troop loses a number of HP required to bring it to the next threshold. If an ability both deals damage and has a non-damaging effect, apply the damage then the rest of the effect."
  - name: "Troop Movement"
    desc: "Whenever a troop moves, you move one of its segments and the other segments follow behind it. At the end of the movement, you can group the other segments adjacent to the one you moved as you see fit, provided none of them moves farther than the moving segment. If you choose not to move the troop any distance, you can instead reshape the position of all the segments as long as one stays in place."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Goblins Burn and Goblins Char!"
    desc: "`pf2:2` The troop's members throw a barrage of burning torches. Each creature in a @Template[type:burst|distance:10] within 30 feet of the troop takes @Damage[2d8[fire]|options:area-damage] damage with a DC 20 [[Reflex]] save. When the troop is reduced to 2 or fewer segments, this area decreases to a @Template[type:burst|distance:5]."
  - name: "Goblins Slash and Goblins Scar!"
    desc: "`pf2:1` `pf2:1` to `pf2:3` <br>  <br> **Frequency** once per round <br>  <br> **Effect** The goblin get gang uses dogslicers, horsechoppers, and burning torches to attack each enemy in a @Template[type:emanation|distance:5], with a DC 20 [[Reflex]] save. The damage depends on the number of actions. <br>  <br> `pf2:1` @Damage[1d6[slashing],1d6[fire]|options:area-damage] damage <br>  <br> `pf2:2` @Damage[(1d6+6)[slashing],1d6[fire]|options:area-damage] damage <br>  <br> `pf2:3` @Damage[(1d6+9)[slashing],1d6[fire]|options:area-damage] damage"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

There is little more terrifying than a goblin raiding party out to take from its neighbors. A swarming mix of commandos, pyros, and war chanters armed with dogslicers, horsechoppers, burning torches, and sharp teeth, this troop enjoys pillaging unprepared communities. Their song is an unsettling counterpart to the screams of their victims.

Goblins can be found across Golarion, sometimes threatening taller humanoids (whom they refer to as "longshanks") and sometimes redeeming harmful history by working alongside others.

```statblock
creature: "Goblin Get Gang"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
