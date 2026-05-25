---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Rancorous Priesthood"
level: "11"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Troop"
trait_04: "Unholy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21"
languages: "Chthonian, Common"
skills:
  - name: Skills
    desc: "Athletics +22, Intimidation +21, Religion +22"
abilityMods: ["+7", "+2", "+6", "+2", "+5", "+4"]
abilities_top:
  - name: "Troop Movement"
    desc: "Whenever a troop moves, you move one of its segments and the other segments follow behind it. At the end of the movement, you can group the other segments adjacent to the one you moved as you see fit, provided none of them moves farther than the moving segment. If you choose not to move the troop any distance, you can instead reshape the position of all the segments as long as one stays in place."
  - name: "Troop Spellcasting"
    desc: "When the rancorous priesthood Casts a Spell, their constituent members combine their efforts into casting a more powerful version of the spell than any one member could achieve alone. When Casting a Spell that has an area of a burst, cone, or line and doesn't have a duration, increase the area of that spell. Add 5 feet to the radius of a burst that normally has a radius of at least 10 feet (a burst with a smaller radius is not affected). Add 5 feet to the length of a cone or line that is normally 15 feet long or smaller, and add 10 feet to the length of a larger cone or line."
armorclass:
  - name: AC
    desc: "31; **Fort** +23, **Ref** +17, **Will** +22"
health:
  - name: HP
    desc: "195; thresholds 130 (3 segments), 65 (2 segments); **Weaknesses** area damage 10, splash damage 10"
abilities_mid:
  - name: "Troop Defenses"
    desc: "**Thresholds** 130 (3 segments), 65 (2 segments) <br>  <br> Troops are composed of many individuals, represented by four \"segments\" on a battle grid. Each segment is 10 feet on each side and as tall as the individual members of the troop. Segments must remain contiguous. Each one has to share at least 5 feet of one of its edges with another segment—being adjacent on a diagonal isn't sufficient! You can measure flanking, cover, and the like using the center of any segment. <br>  <br> A troop has two Hit Point thresholds in its HP entry and loses segments as it crosses thresholds. Typically, the higher threshold is at 2/3 of the troop's maximum Hit Points and the lower is at 1/3 of its maximum. Once the troop drops below the higher threshold, it loses one segment, leaving three segments (12 squares) remaining and setting the first threshold as the troop's new maximum Hit Points. This repeats when the troop drops below the lower threshold, leaving two segments (8 squares). At 0 Hit Points, the troop disperses entirely, with the few remaining members surrendering, [[Fleeing]], or easily dispatched, as determined by the GM. Typically the creature who caused the troop to lose a segment decides which to remove, or the GM decides when a specific creature wasn't responsible. To restore lost segments and maximum Hit Points, a troop needs to spend downtime to use long-term treatment on casualties or recruit new members to replace the fallen. <br>  <br> Troops are typically immune to non-damaging effects that target a single creature, such as a [[Charm]] spell or the [[Demoralize]] action. An ability that can target 5 or more creatures can target an entire segment, increasing to two segments if it can target 10 or more creatures and to the entire troop if it can target 20 or more creatures. An ability that affects all creatures in a certain range affects all segments in range (make any checks or saves separately for each segment). As examples, an 8th rank *charm* spell (with 10 targets) can affect two segments, and an ability that Demoralizes all creatures within 30 feet of you would affect all segments that are fully within that range. A non-damaging ability that would prevent a segment from acting, cause them to flee, or otherwise make them unable to function as part of the troop for a round or more removes the segment entirely. The troop loses a number of HP required to bring it to the next threshold. If an ability both deals damage and has a non-damaging effect, apply the damage then the rest of the effect."
speed: "0 feet"
attacks: []
spellcasting:
  - name: "Divine Spontaneous Spells"
    desc: "DC 30, attack +22<br>**5th** (3 slots) [[Divine Immolation]], [[Shadow Blast]]<br>**2nd** [[Noise Blast]]<br>**1st** [[Daze]], [[Detect Magic]], [[Divine Lance]]"
  - name: "Cleric Domain Spells"
    desc: "DC 30, attack +22<br>**4th** [[Destructive Aura]]<br>**1st** [[Cry of Destruction]]"
abilities_bot:
  - name: "Form Up"
    desc: "`pf2:1` The troop chooses one of the squares it currently occupies and redistributes its squares to any configuration in which all squares are contiguous and within 15 feet of the chosen square. The troop can't share its space with other creatures."
  - name: "Wild Swing"
    desc: "`pf2:1` `pf2:1` to `pf2:3` <br>  <br> **Frequency** once per round <br>  <br> **Effect** The members of the mob wildly swing their weapons in a chaotic attack at each enemy in a @Template[type:emanation|distance:5] with a DC 25 [[Reflex]] save. The damage depends on the number of actions. <br>  <br> `pf2:1` @Damage[(1d12+2)[slashing]|options:area-damage] damage <br>  <br> `pf2:2` @Damage[(2d12+9)[slashing]|options:area-damage] damage <br>  <br> `pf2:3` @Damage[(3d12+9)[slashing]|options:area-damage] damage"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Followers of Rovagug must usually conceal their devotion to the Rough Beast, hiding in remote cave complexes or abandoned ruins, but they emerge when they sense weakness, gathering together into a destructive, homicidal mob to hunt down priests of rival deities or slaughter entire towns.

Religions inspire devout individuals to uphold their tenets.

```statblock
creature: "Rancorous Priesthood"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
