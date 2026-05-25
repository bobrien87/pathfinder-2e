---
type: creature
group: ["Caligni", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Caligni Hunter"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Caligni"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Greater Darkvision]]"
languages: "Caligni, Sakvroth"
skills:
  - name: Skills
    desc: "Acrobatics +13, Athletics +8, Stealth +13, Survival +12, Thievery +11"
abilityMods: ["+2", "+5", "+2", "-1", "+2", "+1"]
abilities_top:
  - name: "At-Will Spells"
    desc: "The monster can cast its at-will spells any number of times without using up spell slots."
  - name: "Sneak Attack"
    desc: "The caligni hunter deals 1d6 extra precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "21; **Fort** +10, **Ref** +13, **Will** +8"
health:
  - name: HP
    desc: "60; final fate"
abilities_mid:
  - name: "Final Fate"
    desc: "When the hunter dies, their soul leaves their body in an explosion of spiritual energy. All creatures in a @Template[burst|distance:20] take @Damage[5d6[spirit]|options:area-damage] damage (DC 19 [[Will]] save). <br>  <br> The hunter's possessions are left in a pile where they died."
  - name: "Light Blindness"
    desc: "When first exposed to bright light, the monster is [[Blinded]] until the end of its next turn. After this exposure, light doesn't blind the monster again until after it spends 1 hour in darkness. However, as long as the monster is in an area of bright light, it's [[Dazzled]]."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +13 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d6+7 piercing plus [[Darkening Poison]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 19, attack +11<br>**2nd** [[Darkness]] (At Will), [[See the Unseen]] (At Will)<br>**1st** [[Figment]]"
abilities_bot:
  - name: "Double Slice"
    desc: "`pf2:2` The caligni hunter makes two Strikes against the same target, one with each of their shortswords. The hunter combines the damage of any attacks that hit and applies precision damage, resistances, and weaknesses only once. Both attacks count toward the hunter's multiple attack penalty, but the penalty increases only after both attacks."
  - name: "Encircling Command"
    desc: "`pf2:1` Each caligni skulker within @Template[emanation|distance:30]{30 feet} of the skulker can Step. Each creeper can benefit from Encircling Command only once per round."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Although caligni hunters are often pressed into leading their skulker kin, most hunters prefer to wander the Darklands or raid the surface free from those responsibilities. Their preferred assaults are usually done by solo caligni hunters or in small groups of two or three.

Calignis lurk in subterranean cities, with each caligni growing into a specific role and form determined by supernatural influences in caligni society. Regardless of their size or role, all calignis are gaunt, with pale flesh and white eyes. Many relish the chance to creep above ground at night to steal resources, shadow their surface counterparts, or simply make mischief.

```statblock
creature: "Caligni Hunter"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
