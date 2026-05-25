---
type: creature
group: ["Caligni", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Caligni Caller"
level: "6"
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
    desc: "+11; [[Greater Darkvision]]"
languages: "Caligni, Sakvroth"
skills:
  - name: Skills
    desc: "Arcana +9, Intimidation +14, Occultism +13, Stealth +15"
abilityMods: ["+2", "+5", "+1", "+1", "+1", "+4"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The caller deals an additional 2d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "24; **Fort** +9, **Ref** +15, **Will** +11"
health:
  - name: HP
    desc: "80; death umbra"
abilities_mid:
  - name: "Death Umbra"
    desc: "When the caller dies, an explosion of shadow devours their body. Each creature in a @Template[emanation|distance:10] must attempt a DC 22 [[Fortitude]] save. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is [[Enfeebled]] 1 for 1 minute. <br> - **Failure** The creature is [[Enfeebled]] 2 and [[Slowed]] 1 for 1 minute."
  - name: "Light Blindness"
    desc: "When first exposed to bright light, the monster is [[Blinded]] until the end of its next turn. After this exposure, light doesn't blind the monster again until after it spends 1 hour in darkness. However, as long as the monster is in an area of bright light, it's [[Dazzled]]."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +15 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+4 piercing plus 1d6 void"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 24, attack +16<br>**5th** [[Umbral Journey]]<br>**3rd** [[Chilling Darkness]]<br>**2nd** [[Darkness]], [[Darkness]] (At Will)<br>**1st** [[Detect Magic]], [[Grim Tendrils]], [[Void Warp]]"
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Although the mysterious demigods known as the Forsaken disappeared eons ago, many calignis continue to follow their ancient traditions of worship.

Owbs, once the Forsaken's servants, still respond to caligni prayers. Caligni callers serve as the priests of their communities, calling upon these shadowy owb patrons for guidance, favors, and power. Their most important ceremony, the blanching, determines the potential of most newborn calignis and shapes their eventual forms.

Due to their close ties to the malevolent owbs, most callers exhibit cruel and inscrutable natures. They often lead caligni enclaves alongside caligni stalkers as spiritual advisors. Callers tend to be highly superstitious, seeing omens everywhere, and they avoid revealing details of their rituals even to other calignis.

Each individual in caligni society serves a specific role. At times, certain roles so rarely find suitable candidates that a community might only see a few individuals fill them in an entire generation.

```statblock
creature: "Caligni Caller"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
