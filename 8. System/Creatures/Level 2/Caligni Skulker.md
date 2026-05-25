---
type: creature
group: ["Caligni", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Caligni Skulker"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Caligni"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Greater Darkvision]]"
languages: "Caligni"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +4, Stealth +10, Thievery +8"
abilityMods: ["+0", "+4", "+3", "-1", "+2", "+1"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The caligni skulker deals 1d6 extra precision damage to [[Off Guard]] creatures."
  - name: "Tumble Behind"
    desc: "When the caligni skulker Tumbles Through a creature's space, that creature is [[Off Guard]] against the next attack the skulker makes against it before the end of its turn."
armorclass:
  - name: AC
    desc: "19; **Fort** +9, **Ref** +10, **Will** +6"
health:
  - name: HP
    desc: "30; final night"
abilities_mid:
  - name: "Final Night"
    desc: "When the caligni skulker dies, their remains dissolve into a @Template[emanation|distance:20] of inky darkness before dissipating. The darkness extinguishes non-magical light sources and attempts to counteract magical light as a 1st-rank effect with a +10 counteract modifier. <br>  <br> The skulker's possessions are left in a pile where they died."
  - name: "Light Blindness"
    desc: "When first exposed to bright light, the monster is [[Blinded]] until the end of its next turn. After this exposure, light doesn't blind the monster again until after it spends 1 hour in darkness. However, as long as the monster is in an area of bright light, it's [[Dazzled]]."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +10 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+4 piercing plus [[Darkening Poison]]"
  - name: "Melee strike"
    desc: "Dagger +10 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4 piercing plus [[Darkening Poison]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Most often found on the surface are caligni skulkers, stealing staple goods and luxuries alike. When pressed into combat by more powerful caligni, skulkers will often be sacrificed in waves to wear down the enemy. Otherwise, skulkers are fairly cautious and prefer to flee unwinnable situations.

Calignis lurk in subterranean cities, with each caligni growing into a specific role and form determined by supernatural influences in caligni society. Regardless of their size or role, all calignis are gaunt, with pale flesh and white eyes. Many relish the chance to creep above ground at night to steal resources, shadow their surface counterparts, or simply make mischief.

```statblock
creature: "Caligni Skulker"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
