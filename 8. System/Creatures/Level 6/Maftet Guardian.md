---
type: creature
group: ["Humanoid", "Maftet"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Maftet Guardian"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Maftet"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Darkvision]]"
languages: "Common, Sphinx"
skills:
  - name: Skills
    desc: "Acrobatics +13, Arcana +13, Athletics +15, Stealth +13, Ruins Lore (Applies Only to Their Home Ruins) +15"
abilityMods: ["+5", "+3", "+4", "+3", "+2", "+0"]
abilities_top:
  - name: "Powerful Scimitars"
    desc: "Any non-magical scimitar becomes a *+1 striking scimitar* while a maftet wields it."
armorclass:
  - name: AC
    desc: "23; **Fort** +14, **Ref** +15, **Will** +12"
health:
  - name: HP
    desc: "90"
abilities_mid:
  - name: "Runic Resistance"
    desc: "`pf2:r` **Trigger** The maftet takes damage from a Strike or spell effect <br>  <br> **Effect** The maftet's protective runic tattoos glow, granting them resistance 5 to one damage type dealt by the triggering attack. <br>  <br> This resistance applies against the triggering effect and lasts for 1 minute or until the maftet uses this ability again, whichever comes first. If the triggering effect deals multiple damage types, the maftet chooses which type to resist. <br>  <br> > [!danger] Effect: Runic Resistance"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Scimitar +17 (`pf2:1`) (forceful, magical, sweep), **Damage** 2d6+8 slashing"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 23, attack +15<br>**1st** [[Sanctuary]], [[Sigil]], [[Sure Strike]]"
abilities_bot:
  - name: "Paired Strike"
    desc: "`pf2:2` **Requirements** The maftet is wielding two scimitars <br>  <br> **Effect** The maftet makes two Strikes against the same target, one with each of their scimitars. The maftet combines the damage of any attacks that hit and applies resistances and weaknesses only once. This counts as one attack when calculating the maftet's multiple attack penalty."
  - name: "Raptor Dive"
    desc: "`pf2:3` **Requirements** The maftet is flying at least 10 feet above the target <br>  <br> **Effect** The maftet Flies up to twice their fly Speed and makes a Paired Strike at the end of the movement. If both Strikes hit, the target is also knocked [[Prone]]."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Maftets are hawk-winged humanoids with leonine lower bodies that dwell in ancient ruins and cities thought lost, typically in desert or mountain regions. They view themselves as guardians and practice a specialized technique of dualwielding scimitars so central to their culture that a maftet's scimitars are often cherished family heirlooms. Most maftets venerate their ancestors in addition to various deities, and even a child can detail their family lineage back multiple generations. Maftet prides tend to be matriarchal and isolationist, though maftets aren't necessarily hostile to outsiders who respect their homes and don't seek to loot them.

When a young maftet comes of age, they receive runic tattoos from a pride's elder. These tattoos are imbued with magic that allows a maftet to enchant their wielded weapons, but the individualized designs tell of the maftet's ancestors, childhood adventures, and positive qualities. Such tattoos are considered sacred and never given to non-maftets.

```statblock
creature: "Maftet Guardian"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
