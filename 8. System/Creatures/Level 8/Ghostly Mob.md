---
type: creature
group: ["Ghost", "Incorporeal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ghostly Mob"
level: "8"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Ghost"
trait_02: "Incorporeal"
trait_03: "Troop"
trait_04: "Undead"
trait_05: "Unholy"
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]]"
languages: "Common, Necril"
skills:
  - name: Skills
    desc: "Acrobatics +16, Stealth +18, Dwelling Lore (applies to the place the mob is bound to) +16"
abilityMods: ["-5", "+4", "+3", "+0", "+4", "+4"]
abilities_top:
  - name: "Site Bound"
    desc: "A ghostly mob can stray no farther than 240 feet from where its members were killed."
armorclass:
  - name: AC
    desc: "25; **Fort** +15, **Ref** +14, **Will** +18"
health:
  - name: HP
    desc: "105; rejuvenation, void healing, Thresholds 70 (3 segments), 35 (2 segments); **Immunities** bleed, death effects, disease, paralyzed, poison, precision, unconscious; **Weaknesses** area damage 8, splash damage 8; **Resistances** all damage 10 except force, ghost touch, spirit, vitality"
abilities_mid:
  - name: "Rejuvenation"
    desc: "When a ghostly mob is destroyed, it re-forms after 2d4 days within the location it's bound to, fully healed. A ghostly mob can be permanently destroyed only if someone sets right whatever prevents the troop from resting."
  - name: "Troop Defenses"
    desc: "**Thresholds** 70 (3 segments), 35 (2 segments) <br>  <br> Troops are composed of many individuals, represented by four \"segments\" on a battle grid. Each segment is 10 feet on each side and as tall as the individual members of the troop. Segments must remain contiguous. Each one has to share at least 5 feet of one of its edges with another segment—being adjacent on a diagonal isn't sufficient! You can measure flanking, cover, and the like using the center of any segment. <br>  <br> A troop has two Hit Point thresholds in its HP entry and loses segments as it crosses thresholds. Typically, the higher threshold is at 2/3 of the troop's maximum Hit Points and the lower is at 1/3 of its maximum. Once the troop drops below the higher threshold, it loses one segment, leaving three segments (12 squares) remaining and setting the first threshold as the troop's new maximum Hit Points. This repeats when the troop drops below the lower threshold, leaving two segments (8 squares). At 0 Hit Points, the troop disperses entirely, with the few remaining members surrendering, [[Fleeing]], or easily dispatched, as determined by the GM. Typically the creature who caused the troop to lose a segment decides which to remove, or the GM decides when a specific creature wasn't responsible. To restore lost segments and maximum Hit Points, a troop needs to spend downtime to use long-term treatment on casualties or recruit new members to replace the fallen. <br>  <br> Troops are typically immune to non-damaging effects that target a single creature, such as a [[Charm]] spell or the [[Demoralize]] action. An ability that can target 5 or more creatures can target an entire segment, increasing to two segments if it can target 10 or more creatures and to the entire troop if it can target 20 or more creatures. An ability that affects all creatures in a certain range affects all segments in range (make any checks or saves separately for each segment). As examples, an 8th rank *charm* spell (with 10 targets) can affect two segments, and an ability that Demoralizes all creatures within 30 feet of you would affect all segments that are fully within that range. A non-damaging ability that would prevent a segment from acting, cause them to flee, or otherwise make them unable to function as part of the troop for a round or more removes the segment entirely. The troop loses a number of HP required to bring it to the next threshold. If an ability both deals damage and has a non-damaging effect, apply the damage then the rest of the effect."
  - name: "Troop Movement"
    desc: "Whenever a troop moves, you move one of its segments and the other segments follow behind it. At the end of the movement, you can group the other segments adjacent to the one you moved as you see fit, provided none of them moves farther than the moving segment. If you choose not to move the troop any distance, you can instead reshape the position of all the segments as long as one stays in place."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Clutching Hands"
    desc: "`pf2:1` `pf2:1` to `pf2:3` <br>  <br> **Frequency** once per round <br>  <br> **Effect** The troop attacks enemies in a @Template[type:emanation|distance:5], with a DC 23 [[Reflex]] save. The damage depends on the number of actions. <br>  <br> `pf2:1` @Damage[(1d6+3)[void]|options:area-damage] damage <br>  <br> `pf2:2` @Damage[(3d6+6)[void]|options:area-damage] damage <br>  <br> `pf2:3` @Damage[(4d6+9)[void]|options:area-damage] damage"
  - name: "Frightful Chorus"
    desc: "`pf2:2` The ghostly mob howls in anguish, sharing the pain of their death with any living creature that can hear them. This painful wailing forces each living creature in a @Template[type:emanation|distance:30] to attempt a DC 26 [[Will]] save or become [[Frightened]] 2 ([[Frightened]] 3 on a critical failure). Regardless of the save result, the creature is then temporarily immune to the troop's Frightful Chorus for 1 minute."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

When a horrific tragedy results in mass death, the restless spirits of the numerous dead might arise as a ghostly mob. Like other ghosts, ghostly mobs are often unaware they're dead. The spirits trapped within the mob can try to carry out a semblance of their former lives, even though their memories are fragmentary and their forms are insubstantial. This fragmented memory revolves around their last moments in that location, which compels the ghosts to instinctually play out these last moments, sometimes ranging from a few minutes to entire days' worth of time. When one or more of the members of a ghostly mob are forced to confront their undead nature, the spirits lash out in pain and violence.

Tethered to the world after death by powerful emotions that haven't been resolved, ghosts haunt the living as sad echoes of their former selves. Rules for creating a ghost start on page 160 of Monster Core.

```statblock
creature: "Ghostly Mob"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
