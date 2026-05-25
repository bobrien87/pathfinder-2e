---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Watchmage Squadron"
level: "10"
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
    desc: "+22"
languages: "Common"
skills:
  - name: Skills
    desc: "Arcana +21, Athletics +19, Intimidation +20, Society +19, Legal Lore +21"
abilityMods: ["+3", "+4", "+3", "+5", "+2", "+0"]
abilities_top:
  - name: "Invisibility Scan"
    desc: "Invisibility can't make anything [[Undetected]] or [[Unnoticed]] to the watchmage squadron."
  - name: "Troop Spellcasting"
    desc: "When the watchmage squadron Casts a Spell, the individual members combine their efforts into casting a more powerful version than any one member could achieve alone. When Casting a Spell that has an area of a burst, cone, or line and doesn't have a duration, increase the area of that spell. Add 5 feet to the radius of a burst that normally has a radius of at least 10 feet (a burst with a smaller radius is not affected). Add 5 feet to the length of a cone or line that is normally 15 feet long or smaller, and add 10 feet to the length of a larger cone or line."
armorclass:
  - name: AC
    desc: "30; **Fort** +22, **Ref** +16, **Will** +19"
health:
  - name: HP
    desc: "180; **Weaknesses** area damage 10, splash damage 10"
abilities_mid:
  - name: "Troop Defenses"
    desc: "**Thresholds** 120 (3 segments), 60 (2 segments) <br>  <br> Troops are composed of many individuals, represented by four \"segments\" on a battle grid. Each segment is 10 feet on each side and as tall as the individual members of the troop. Segments must remain contiguous. Each one has to share at least 5 feet of one of its edges with another segment—being adjacent on a diagonal isn't sufficient! You can measure flanking, cover, and the like using the center of any segment. <br>  <br> A troop has two Hit Point thresholds in its HP entry and loses segments as it crosses thresholds. Typically, the higher threshold is at 2/3 of the troop's maximum Hit Points and the lower is at 1/3 of its maximum. Once the troop drops below the higher threshold, it loses one segment, leaving three segments (12 squares) remaining and setting the first threshold as the troop's new maximum Hit Points. This repeats when the troop drops below the lower threshold, leaving two segments (8 squares). At 0 Hit Points, the troop disperses entirely, with the few remaining members surrendering, [[Fleeing]], or easily dispatched, as determined by the GM. Typically the creature who caused the troop to lose a segment decides which to remove, or the GM decides when a specific creature wasn't responsible. To restore lost segments and maximum Hit Points, a troop needs to spend downtime to use long-term treatment on casualties or recruit new members to replace the fallen. <br>  <br> Troops are typically immune to non-damaging effects that target a single creature, such as a [[Charm]] spell or the [[Demoralize]] action. An ability that can target 5 or more creatures can target an entire segment, increasing to two segments if it can target 10 or more creatures and to the entire troop if it can target 20 or more creatures. An ability that affects all creatures in a certain range affects all segments in range (make any checks or saves separately for each segment). As examples, an 8th rank *charm* spell (with 10 targets) can affect two segments, and an ability that Demoralizes all creatures within 30 feet of you would affect all segments that are fully within that range. A non-damaging ability that would prevent a segment from acting, cause them to flee, or otherwise make them unable to function as part of the troop for a round or more removes the segment entirely. The troop loses a number of HP required to bring it to the next threshold. If an ability both deals damage and has a non-damaging effect, apply the damage then the rest of the effect."
  - name: "Troop Movement"
    desc: "Whenever a troop moves, you move one of its segments and the other segments follow behind it. At the end of the movement, you can group the other segments adjacent to the one you moved as you see fit, provided none of them moves farther than the moving segment. If you choose not to move the troop any distance, you can instead reshape the position of all the segments as long as one stays in place."
speed: "0 feet"
attacks: []
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 26, attack +18<br>**5th** (3 slots) [[Fireball]], [[Locate]], [[Slither]]<br>**4th** (2 slots) [[Dispel Magic]], [[Grim Tendrils]]<br>**2nd** (1 slots) [[Revealing Light]]<br>**Cantrips** [[Detect Magic]], [[Frostbite]], [[Light]], [[Tangle Vine]]"
abilities_bot:
  - name: "Bash Heads"
    desc: "`pf2:2` The watchmages lash out against all enemies in a @Template[type:emanation|distance:5] with their fists, dealing @Damage[(4d4+4)[bludgeoning]|options:area-damage] damage with a DC 29 [[Reflex]] save."
  - name: "Fire Shortbows!"
    desc: "`pf2:1` `pf2:1` to `pf2:3` <br>  <br> **Frequency** once per round <br>  <br> **Effect** The watchmages fire a volley against each enemy in a @Template[type:burst|distance:10] within 150 feet, with a DC 26 [[Reflex]] save. The damage depends on the number of actions. When the squadron is reduced to 2 or fewer segments, this area decreases to a @Template[type:burst|distance:5]. <br>  <br> `pf2:1` @Damage[(1d6+3)[piercing],1d6[force]|options:area-damage]{1d6+3 piercing plus 1d6 force} damage <br>  <br> `pf2:2` @Damage[(3d6+6)[piercing],1d6[force]|options:area-damage]{3d6+6 piercing plus 1d6 force} damage <br>  <br> `pf2:3` @Damage[(4d6+6)[piercing],1d6[force]|options:area-damage]{4d6+6 piercing plus 1d6 force} damage"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Governments often organize and deploy squadrons of watchmages in places where dangerous magic is expected. Members combine their spellcasting to cast at a higher level than they could alone.

Larger societies rely on those with the authority and the ability to interpret and enforce laws. Some carry out these duties fairly, but others are harsh and cruel, imposing severe punishments on anyone unable to pay for clemency.

```statblock
creature: "Watchmage Squadron"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
