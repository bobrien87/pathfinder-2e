---
type: creature
group: ["Azata", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Veranallia"
level: "20"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Azata"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+38; [[Darkvision]], [[Tremorsense]] (imprecise) 120 feet"
languages: "Diabolic, Draconic, Empyrean (speak with animals, speak with plants, tongues)"
skills:
  - name: Skills
    desc: "Athletics +34, Deception +36, Diplomacy +38, Intimidation +36, Medicine +36, Nature +34, Survival +38, Elysium Lore +36"
abilityMods: ["+8", "+6", "+8", "+6", "+10", "+8"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Rebirth"
    desc: "**Frequency** once per day <br>  <br> **Effect** The veranallia spends a minute to encase a creature that has been dead for no more than a year in a cocoon. After 24 hours, the creature is restored to life, and the cocoon explodes in a shower of colorful blossoms. If the veranallia's chooses, Rebirth can change the creature's ancestry or heritage, typically into an nephilim."
armorclass:
  - name: AC
    desc: "45; **Fort** +36, **Ref** +34, **Will** +38"
health:
  - name: HP
    desc: "475; **Weaknesses** cold iron 20, unholy 20; **Resistances** fire 20, cold 20"
abilities_mid:
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Sickle +36 (`pf2:1`) (agile, finesse, holy, magical, trip), **Damage** 3d4+12 slashing plus 4d6 cold plus 1d6 spirit"
  - name: "Melee strike"
    desc: "Vine +36 (`pf2:1`) (holy, magical, reach 20 ft.), **Damage** 4d12+16 bludgeoning plus 1d6 spirit plus [[Improved Grab]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 42, attack +34<br>**10th** [[Cataclysm]], [[Manifestation (once per year)]], [[Revival]]<br>**9th** [[Nature's Enmity]], [[Wrathful Storm]]<br>**8th** [[Arctic Rift]] (At Will)<br>**7th** [[Regenerate]], [[Sunburst]] (At Will)<br>**6th** [[Cursed Metamorphosis]] (At Will), [[Tangling Creepers]] (At Will)<br>**5th** [[Nature's Pathway]] (At Will), [[Truespeech]] (Constant)<br>**3rd** [[Speak with Plants]] (Constant)<br>**2nd** [[Speak with Animals]] (Constant)"
abilities_bot:
  - name: "Alter Weather"
    desc: "`pf2:3` **Frequency** three times per day <br>  <br> **Effect** The veranallia dramatically alters weather patterns in the surrounding area, producing any of the results of a successful 9th-rank [[Control Weather]] ritual."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Veranallias represent the freedom of life to grow, change, and adapt. They rarely interact directly with non-azatas, as most other beings find their nature hard to comprehend, but those who secure their aid find them powerful allies. The lower half of a veranallia's body is made of vegetation that constantly repeats a dizzying cycle of sprouting, blooming, thriving, and wilting. The upper half of their body appears as that of a humanoid of any gender-it is rare for a veranallia to remain consistent in their gender for more than a few seasons at a time.

Veranallias transform the landscape in their wake, bringing creation and destruction alike. The world around them overflows with an abundance of vegetation, with plenty of food for nearby animals, and when they bring destruction, they do so without cruelty, as it is sometimes necessary to make room for new life. They trigger forest fires in woodlands before dry brush piles up to dangerous levels, and bring bitter winters to areas plagued with parasites that thrive in hot weather.

```statblock
creature: "Veranallia"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
