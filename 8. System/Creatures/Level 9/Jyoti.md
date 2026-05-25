---
type: creature
group: ["Fire", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Jyoti"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Fire"
trait_02: "Humanoid"
trait_03: "Vitality"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Darkvision]]"
languages: "Common, Jyoti"
skills:
  - name: Skills
    desc: "Acrobatics +20, Intimidation +18, Occultism +20, Society +18"
abilityMods: ["+3", "+5", "+4", "+5", "+6", "+3"]
abilities_top:
  - name: "Infuse Weapons"
    desc: "Any weapon a jyoti wields becomes a *[[Flaming]] [[Ghost Touch]]* weapon while the jyoti holds it."
armorclass:
  - name: AC
    desc: "28; **Fort** +15, **Ref** +18, **Will** +21"
health:
  - name: HP
    desc: "155; **Immunities** death effects, disease, poison; **Resistances** fire 10, void 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "+2 Status to All Saves vs. Divine Magic"
    desc: ""
  - name: "Vitality Energy Affinity"
    desc: "Vitality healing effects always heal the jyoti for the maximum amount. It doesn't gain the automatic Hit Points or temporary Hit Points from being on a plane with the vitality planar essence trait."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Flaming Ghost Touch Longspear +20 (`pf2:1`) (magical, reach 10 ft.), **Damage** 2d8+6 piercing"
  - name: "Melee strike"
    desc: "Beak +21 (`pf2:1`) (finesse), **Damage** 2d12+6 piercing"
  - name: "Melee strike"
    desc: "Talon +21 (`pf2:1`) (agile, finesse), **Damage** 2d8+6 slashing"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 0, attack +0<br>**5th** [[Banishment]], [[Breath of Life]]<br>**4th** [[Translocate]]<br>**3rd** [[Holy Light]]<br>**2nd** [[Cleanse Affliction]], [[Clear Mind]], [[Sound Body]]<br>**1st** [[Heal]], [[Heal]], [[Light]], [[Vitality Lash]]"
abilities_bot:
  - name: "Breath of Burning Life"
    desc: "`pf2:2` The jyoti breathes a blast of searing flame infused with vitality energy in a @Template[type:cone|distance:40] that deals @Damage[8d6[fire]|options:area-damage] damage plus @Damage[4d6[vitality]|options:area-damage] damage to creatures in the area (DC 28 [[Reflex]] save). The jyoti can't use Breath of Burning Life again for 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Jyotis are sometimes called "false phoenixes" (a term they find insulting) by the ignorant or willful. These avian humanoids are native to Creation's Forge, where they are the caretakers of the tree-sized, crystalline flowers within the Garden of Creation's Forge. These physical manifestations of mortal souls that ascended to divinity are protected and venerated by jyotis. They rarely leave this enigmatic realm and view visitors from other planes as stains on the purity of their home. Jyotis particularly distrust divine spellcasters and religious warriors, seeing them as inclined to take credit for manifesting a life force that, from a jyoti's perspective, is as plentiful and ubiquitous as water is to fish.

Despite their distrust of intruders, jyotis rarely attack unprovoked when their homes are not threatened. However, they don't tolerate intruders into their palace dwelling of crystallized light and captured flame. They often chase even those who come bearing gifts away; few visitors have anything they desire, for what they desire most is to be left alone. Jyotis' full wrath is reserved for natives of the Netherworld and the Void. Historically, the promise of battle with the gargoyle-like sceaduinars, whom they consider it their duty to oppose, has been the only thing to lure jyoti armies beyond Creation's Forge.

```statblock
creature: "Jyoti"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
