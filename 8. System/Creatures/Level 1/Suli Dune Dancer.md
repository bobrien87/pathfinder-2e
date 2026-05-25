---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Suli Dune Dancer"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Suli"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5"
languages: "Common, Petran, Pyric, Sussuran, Thalassic"
skills:
  - name: Skills
    desc: "Acrobatics +5, Deception +6, Diplomacy +7, Occultism +4, Performance +7, Society +4"
abilityMods: ["+2", "+2", "+0", "+1", "+0", "+4"]
abilities_top: []
armorclass:
  - name: AC
    desc: "15; **Fort** +3, **Ref** +5, **Will** +5"
health:
  - name: HP
    desc: "16"
abilities_mid:
  - name: "Elemental Bulwark"
    desc: "`pf2:r` **Trigger** An enemy is about to damage the dune dancer with cold, electricity, or fire, or with a spell that has the air, earth, fire, or water trait <br>  <br> **Effect** The dune dancer gain resistance 2 against the triggering damage"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Scimitar +7 (`pf2:1`) (forceful, sweep), **Damage** 1d6+2 slashing"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 17, attack +9<br>**1st** (2 slots) [[Detect Magic]], [[Dizzying Colors]], [[Guidance]], [[Shield]], [[Soothe]], [[Sure Strike]], [[Telekinetic Hand]], [[Telekinetic Projectile]]"
abilities_bot:
  - name: "Distracting Dance"
    desc: "`pf2:1` With a twirl of their body or with elaborate hand movements, the suli dune dancer attempts to distract a creature within 30 feet. The dune dance attempts a Performance check against the target's Perception DC. <br> - **Critical Success** The target is [[Off Guard]] and takes a –2 circumstance bonus to Perception checks until the end of the dune dancer's next turn. <br> - **Success** The target is off-guard until the end of the dune dancer's current turn. <br> - **Critical Failure** The dune dancer is off-guard against attacks from the target until the end of their next turn."
  - name: "Elemental Assault"
    desc: "`pf2:2` Elemental magic fills the dune dancer's body or weapon. The dune dancer chooses one element and makes a melee Strike. The Strike deals an additional 1d4 damage of the indicated type and has the trait corresponding to the element: <br>  <br> - **Air** electricity <br>  <br> - **Earth** bludgeoning <br>  <br> - **Fire** fire <br>  <br> - **Metal** slashing <br>  <br> - **Water** cold <br>  <br> - **Wood** vitality"
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Because their genie forebears travel all across the Universe, sulis (scions of mortals and jann, who are composed of all six elements) are by and large the most common geniekin on that plane. They're often artisans and peace brokers, compelled to try and bring harmony and balance in a world wrought with discord.

Sulis have a natural charm that often eludes other geniekin, but they tend to layer on a level of boastful pride or even arrogance as a personal quirk or humorous facade. Few non-sulis realize that bragging isn't simply the symptom of a puffed-up ego for sulis, but instead a cultural institution easily comparable to human poetry. Sulis' boasts not only glorify themselves but also secure their companions' and families' accomplishments in history, with the ultimate goal of spinning stories that will be retold for generations. This is especially true for sulis who have lived with other geniekin and have been seen as lesser for not having a strong connection to an Elemental Plane.

Suli dune dancers are but one way these geniekin seek to integrate with other humanoid societies. They work to hone their skills at boasting to an extent that their claims help bolster those they travel with. Suli from regions other than deserts adjust their names to match their terrains, but regardless of whether they prefer forests, hills, or arctic plains, their boasts remain as compelling.

```statblock
creature: "Suli Dune Dancer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
