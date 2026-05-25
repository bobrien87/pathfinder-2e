---
type: creature
group: ["Dhampir", "Human"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dhampir Wizard"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Dhampir"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+4; [[Darkvision]]"
languages: "Common, Necril"
skills:
  - name: Skills
    desc: "Acrobatics +7, Arcana +8, Deception +5, Intimidation +5, Society +8, Stealth +7, Vampire Lore +8"
abilityMods: ["+2", "+3", "+0", "+4", "+0", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +4, **Ref** +7, **Will** +6"
health:
  - name: HP
    desc: "22; void healing"
abilities_mid:
  - name: "+2 Circumstance to All Saves vs. Disease"
    desc: ""
  - name: "Blood of the Night"
    desc: "The dhampir's penalty and Hit Point reduction from the [[Drained]] condition are reduced as though the condition value were 1 lower."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +6 (`pf2:1`) (two hand d8), **Damage** 1d6+2 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+2 bludgeoning"
  - name: "Melee strike"
    desc: "Dagger +7 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+2 piercing"
  - name: "Melee strike"
    desc: "Dagger +7 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+2 piercing"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 18, attack +8<br>**1st** (4 slots) [[Command]], [[Force Barrage]], [[Grim Tendrils]], [[Grim Tendrils]]<br>**Cantrips** [[Detect Magic]], [[Frostbite]], [[Prestidigitation]], [[Shield]], [[Void Warp]]"
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

This dhampir is a svetocher, the child of a moroi vampire.

As the mortal offspring of a vampire and a living parent, dhampirs occupy an unusual place among the living. Their vampiric parentage lends them elongated incisors, an unearthly beauty and physical grace, ghostly pallor, and a piercing gaze. Perhaps their most distinctive feature, however, is their connection to energy from the Void, which heals them, leaving them as vulnerable to life energy as any undead creature. Though they don't suffer the full range of a vampire's vulnerabilities, they do share certain characteristics with their vampire parent, leading to several distinct dhampir heritages across Golarion. By far the most common dhampirs are svetochers, the children of the more common moroi vampires.

Many dhampirs grow up as orphans because their mortal parent perished as a result of a difficult childbirth, or else they believed their child to be cursed and abandoned them. Often outcast, some dhampirs leverage their charisma and personal magnetism to manipulate those around them, while others struggle to form even basic relationships. Mistrust of a dhampir's ancestry presents further challenges when dhampirs attempt to integrate into mortal society. Those who seek out their vampiric parent often find themselves judged as inferior, rejected as they were by mortals but for different reasons. But in regions like Nidal, Geb, and Ustalav, where vampires are viewed with some degree of respect, dhampirs can find their heritage empowering.

Dhampirs fill countless roles within many communities. Some prefer to blend in as best they can, holding regular jobs and building families (most children born to dhampirs share an ancestry with the dhampir's mortal parent, but a rare few are born as dhampirs themselves). Those who learn to make the most of their inherited charm can achieve high societal status, whether leveraging traditional avenues of power or gathering followers enamored by the dhampir's abilities. With a lifespan rivaling that of an elf, a dhampir can develop extensive influence and engage in long-reaching schemes of massive scope. Further, their ancestry lends them a proclivity to necromancy and the occult arts.

```statblock
creature: "Dhampir Wizard"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
