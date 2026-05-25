---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Bandit Gang"
level: "7"
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
    desc: "+15"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +16, Deception +14, Intimidation +16, Stealth +17, Survival +11, Thievery +16"
abilityMods: ["+3", "+5", "+2", "+1", "+2", "+3"]
abilities_top:
  - name: "Lie in Wait"
    desc: "The troop can spend 10 minutes preparing the ground before combat to gain a +2 circumstance bonus to their initiative roll."
  - name: "Sudden Ambush"
    desc: "When the troop rolls initiative using Deception or Stealth, they can use Stand and Deliver! as a free action."
  - name: "Forest Passage"
    desc: "The bandit gang ignores any difficult terrain caused by plants, such as bushes, vines, and undergrowth."
  - name: "Troop Movement"
    desc: "Whenever a troop moves, you move one of its segments and the other segments follow behind it. At the end of the movement, you can group the other segments adjacent to the one you moved as you see fit, provided none of them moves farther than the moving segment. If you choose not to move the troop any distance, you can instead reshape the position of all the segments as long as one stays in place."
armorclass:
  - name: AC
    desc: "24; **Fort** +15, **Ref** +16, **Will** +13"
health:
  - name: HP
    desc: "120; Thresholds 80 (3 segments), 40 (2 segments); **Weaknesses** area damage 8, splash damage 8"
abilities_mid:
  - name: "Troop Defenses"
    desc: "**Thresholds** 80 (3 segments), 40 (2 segments) <br>  <br> Troops are composed of many individuals, represented by four \"segments\" on a battle grid. Each segment is 10 feet on each side and as tall as the individual members of the troop. Segments must remain contiguous. Each one has to share at least 5 feet of one of its edges with another segment—being adjacent on a diagonal isn't sufficient! You can measure flanking, cover, and the like using the center of any segment. <br>  <br> A troop has two Hit Point thresholds in its HP entry and loses segments as it crosses thresholds. Typically, the higher threshold is at 2/3 of the troop's maximum Hit Points and the lower is at 1/3 of its maximum. Once the troop drops below the higher threshold, it loses one segment, leaving three segments (12 squares) remaining and setting the first threshold as the troop's new maximum Hit Points. This repeats when the troop drops below the lower threshold, leaving two segments (8 squares). At 0 Hit Points, the troop disperses entirely, with the few remaining members surrendering, [[Fleeing]], or easily dispatched, as determined by the GM. Typically the creature who caused the troop to lose a segment decides which to remove, or the GM decides when a specific creature wasn't responsible. To restore lost segments and maximum Hit Points, a troop needs to spend downtime to use long-term treatment on casualties or recruit new members to replace the fallen. <br>  <br> Troops are typically immune to non-damaging effects that target a single creature, such as a [[Charm]] spell or the [[Demoralize]] action. An ability that can target 5 or more creatures can target an entire segment, increasing to two segments if it can target 10 or more creatures and to the entire troop if it can target 20 or more creatures. An ability that affects all creatures in a certain range affects all segments in range (make any checks or saves separately for each segment). As examples, an 8th rank *charm* spell (with 10 targets) can affect two segments, and an ability that Demoralizes all creatures within 30 feet of you would affect all segments that are fully within that range. A non-damaging ability that would prevent a segment from acting, cause them to flee, or otherwise make them unable to function as part of the troop for a round or more removes the segment entirely. The troop loses a number of HP required to bring it to the next threshold. If an ability both deals damage and has a non-damaging effect, apply the damage then the rest of the effect."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Chop 'em Down!"
    desc: "`pf2:1` `pf2:1` to `pf2:3` <br>  <br> **Frequency** once per round <br>  <br> **Effect** The bandits make a coordinated attack with their axes against each enemy in a @Template[emanation|distance:5] with a DC 22 [[Reflex]] save. The damage depends on the number of actions. <br>  <br> `pf2:1` @Damage[(1d6+3)[slashing]|options:area-damage] damage <br>  <br> `pf2:2` @Damage[(2d6+9)[slashing]|options:area-damage] damage <br>  <br> `pf2:3` @Damage[(3d6+9)[slashing]|options:area-damage] damage"
  - name: "Launch Slings!"
    desc: "`pf2:2` The bandits draw or reload their slings, then launch a volley of sling bullets. This is a @Template[burst|distance:10] within 50 feet that deals @Damage[(2d6+4)[bludgeoning]|options:area-damage] damage with a DC 22 [[Reflex]] save. When the troop is reduced to 2 or fewer segments, this area decreases to a @Template[burst|distance:5]."
  - name: "Stand and Deliver!"
    desc: "`pf2:1` The troop attempts to `act demoralize` up to 4 creatures."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Cutthroat crews of criminals form gangs to take out larger scores and intimidate their victims. Bandit gangs are often accompanied by a [[Gang Leader]].

In the underbelly of society, the lawless reign supreme.

```statblock
creature: "Bandit Gang"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
