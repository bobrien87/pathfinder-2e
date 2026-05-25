---
type: creature
group: ["Beast", "Troll"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Trollhound"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Beast"
trait_02: "Troll"
trait_03: "Wood"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +6, Athletics +9, Stealth +8, Survival +6"
abilityMods: ["+4", "+1", "+5", "-3", "+1", "-2"]
abilities_top:
  - name: "Bloodfire Fever"
    desc: "Trollhounds and trolls are immune to bloodfire fever <br>  <br> **Saving Throw** DC 18 [[Fortitude]] save <br>  <br> **Stage 1** carrier with no ill effect (1 day) <br>  <br> **Stage 2** [[Enfeebled]] 1 (1 day) <br>  <br> **Stage 3** enfeebled 1 and [[Clumsy]] 1 (1 day) <br>  <br> **Stage 4** [[Enfeebled]] 2 and [[Clumsy]] 2 (1 day) <br>  <br> **Stage 5** enfeebled 2, clumsy 2, and [[Fatigued]] (1 day)"
  - name: "Pack Attack"
    desc: "The trollhound deals an extra 1d6 damage to any creature within reach of at least two of the trollhound's allies."
armorclass:
  - name: AC
    desc: "17; **Fort** +14, **Ref** +8, **Will** +6"
health:
  - name: HP
    desc: "65; regeneration 15 (deactivated by electricity or fire); **Weaknesses** electricity 8, fire 8"
abilities_mid:
  - name: "Regeneration 15 (Deactivated by Electricity or Fire)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Flailing Bite"
    desc: "`pf2:r` **Trigger** The trollhound takes electricity or fire damage <br>  <br> **Effect** The trollhound makes a jaws Strike against a random creature within reach. If the trollhound has persistent fire damage, they attempt a DC 15 flat check to remove it."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +11 (`pf2:1`) (unarmed), **Damage** 1d12+4 piercing plus [[Bloodfire Fever]] plus [[Knockdown]]"
spellcasting: []
abilities_bot:
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Trollhounds are squat, slavering beasts akin to trolls in canine form. With a similar nigh-insatiable hunger stoked by their regenerative metabolisms, packs of wild trollhounds prowl the foothills of regions where trolls dwell to hunt for vast quantities of meat. In some regions, trolls breed trollhounds as pets, utilizing the trollhounds' keen sense of smell to aid in the hunt.

Covered in fetid, weeping sores, trollhounds are carriers of a debilitating contagion known as bloodfire fever. Creatures that contract the disease through the bite of a trollhound experience deep internal pain, as if their blood were on fire. Additional symptoms include loss of muscle coordination, pus-filled blisters, and overall lethargy and fatigue. Other than living with the pain from skin irritation, both trolls and trollhounds are immune to the major effects of the disease.

Trollhounds are fearless on the hunt and in combat, relying on their ability to regenerate to carry them through. Not even the threat of fire is enough to repel them, as the beasts don't recognize the danger it represents. Nevertheless, fire is one of the most effective tools in combating trollhounds; canny hunters know to burn every last remnant of a supposedly slain trollhound, for their regenerative powers are potent indeed.

While trolls have had great success in domesticating, training, and even befriending trollhounds, the same can't be said for other would-be masters. Whether impeded by constant exposure to trollhounds' diseased slobber, their ravenous hunger that never seems to be fully sated, or simply their foul personality and quick-to-bite temperament, most attempts to use trollhounds in place of more reliable guardians end in pain, misery, and a pack of feral trollhounds escaping into the hinterlands.

Left to their own devices, trollhounds will breed relatively quickly. It can take less than a year for a small pack to multiply into such a size that they pose a significant threat to the countryside. Best to leave the trollhounds to the trolls, as they say!

```statblock
creature: "Trollhound"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
