---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dedicated Druid"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Lifesense]] (imprecise) 30 feet"
languages: "Common, Wildsong"
skills:
  - name: Skills
    desc: "Diplomacy +14, Intimidation +12, Nature +17, Religion +15, Stealth +13, Survival +17"
abilityMods: ["+4", "+2", "+1", "+1", "+4", "+1"]
abilities_top:
  - name: "Plant Empathy"
    desc: "The dedicated druid can ask questions of, receive answers from, and use the Diplomacy skill with plants and fungus."
armorclass:
  - name: AC
    desc: "24; **Fort** +12, **Ref** +13, **Will** +15"
health:
  - name: HP
    desc: "100"
abilities_mid:
  - name: "Shield Block"
    desc: "`pf2:r` **Trigger** The monster has its shield raised and takes damage from a physical attack. <br>  <br> **Effect** The monster snaps its shield into place to deflect a blow. The shield prevents the monster from taking an amount of damage up to the shield's Hardness. The monster and the shield each take any remaining damage, possibly breaking or destroying the shield."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Spear +16 (`pf2:1`) (magical), **Damage** 1d6+8 piercing"
  - name: "Melee strike"
    desc: "Spear +14 (`pf2:1`) (magical, thrown 20), **Damage** 1d6+8 piercing"
  - name: "Melee strike"
    desc: "Fist +15 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+8 bludgeoning"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 25, attack +17<br>**4th** (2 slots) [[Fly]], [[Lightning Bolt]]<br>**3rd** (3 slots) [[Earthbind]], [[Fireball]], [[Wall of Thorns]]<br>**2nd** (3 slots) [[Entangling Flora]], [[Mist]], [[One with Plants]]<br>**1st** (3 slots) [[Air Bubble]], [[Gentle Landing]], [[Gust of Wind]]<br>**Cantrips** [[Electric Arc]], [[Ignition]], [[Know the Way]], [[Tangle Vine]], [[Vitality Lash]]"
  - name: "Druid Order Spells"
    desc: "DC 25, attack +0<br>**1st** [[Cornucopia]]"
abilities_bot:
  - name: "Nature's Patient Healing"
    desc: "`pf2:3` **Requirements** The dedicated druid is in a natural environment <br>  <br> **Effect** The dedicated druid camouflages themself to blend in with the surrounding area, sprouting leaves or covering themself with scree. They gain Concealment until the end of their next turn, they can `act hide options=natures-patient-healing` with a +4 circumstance bonus, and they recover 4d8 healing Hit Points. If the druid moves or otherwise leaves their space, these benefits end."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Individuals who dedicate their life to the protection and preservation of the natural world often become druids. These devoted practitioners of primal magic might work alone or in a circle of like-minded individuals, all of whom have primal powers more terrifying than the last.

A primalist is a wielder of primal energies and magic, sometimes taught by forces of primal power, including powerful elementals or fey of the First World. Primalists protect the natural world, offering strong medicine to those in need while facing suspicion from those who don't understand their ways.

A great many primalists belong to druidic circles, and even those who aren't members tend to be familiar with the most prominent ones in their homeland.

```statblock
creature: "Dedicated Druid"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
