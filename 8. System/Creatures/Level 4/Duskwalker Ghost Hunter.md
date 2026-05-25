---
type: creature
group: ["Duskwalker", "Human"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Duskwalker Ghost Hunter"
level: "4"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Duskwalker"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]]"
languages: "Common, Necril"
skills:
  - name: Skills
    desc: "Acrobatics +10, Athletics +8, Deception +6, Intimidation +6, Nature +8, Stealth +12, Survival +8"
abilityMods: ["+2", "+4", "+1", "+0", "+2", "+0"]
abilities_top:
  - name: "Ghost Hunter"
    desc: "The duskwalker's weapons have the benefits of the *[[Ghost Touch]]* property rune on attacks against incorporeal undead."
armorclass:
  - name: AC
    desc: "21 (22 against prey; see Spirit Hunter); **Fort** +9, **Ref** +12, **Will** +10"
health:
  - name: HP
    desc: "56; **Resistances** void 2"
abilities_mid:
  - name: "+1 Status to All Saves vs. Death Effects"
    desc: ""
  - name: "Ghost Dodge"
    desc: "`pf2:r` **Trigger** The duskwalker is targeted by a Strike or spell <br>  <br> **Effect** The duskwalker gains a +2 circumstance bonus to AC, resistance 5 to spirit damage, and increases their resistance to void damage to 5, all against the triggering attack."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Hatchet +12 (`pf2:1`) (agile, sweep), **Damage** 1d6+5 slashing"
  - name: "Melee strike"
    desc: "Hatchet +14 (`pf2:1`) (agile, sweep, thrown 10), **Damage** 1d6+5 slashing"
  - name: "Ranged strike"
    desc: "Composite Longbow +14 (`pf2:1`) (deadly d10, propulsive, reload 0, volley 30, range 100 ft.), **Damage** 1d8+4 piercing"
spellcasting: []
abilities_bot:
  - name: "Spirit Hunter"
    desc: "`pf2:1` The duskwalker designates a single creature they can observe as their prey. <br>  <br> The duskwalker gains a +2 circumstance bonus to Deception checks, Intimidation checks, and Stealth checks against their prey and to any check to Recall Knowledge about it, and deal an additional 2 spirit damage with all weapon Strikes against their prey. <br>  <br> These effects last until the duskwalker uses Spirit Hunter again."
  - name: "Spirit Shot"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Requirements** The duskwalker has designated a creature as their prey using Spirit Hunter <br>  <br> **Effect** The duskwalker makes two ranged Strikes against their prey. If both Strikes hit, combine their damage for the purpose of resistances and weaknesses."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Duskwalkers are infused with the same energies as psychopomps. These ashen scions are reborn in the mortal Universe to guard the cycle of life and death.

Many immortals dwell upon the other planes of the Great Beyond. Some are benevolent and kind, like angels. Others are cruel and destructive, like demons. And some fit roles outside of morality, like psychopomps. It's far from unheard of for mortals and immortals alike to become entangled romantically, and the children of such engagements carry a supernatural element in their bloodlines for generations to follow. After the first generation, this otherworldly influence usually lies dormant, but now and then, the influence can manifest strongly in descendants many years later. These inheritors of extraplanar legacies are known collectively as planar scions.

```statblock
creature: "Duskwalker Ghost Hunter"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
