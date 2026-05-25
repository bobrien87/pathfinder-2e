---
type: creature
group: ["Kami", "Spirit"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Zuishin"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Kami"
trait_02: "Spirit"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Darkvision]]"
languages: "Common, Empyrean (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +23, Athletics +22, Intimidation +19, Medicine +21, Nature +21, Stealth +21"
abilityMods: ["+6", "+7", "+5", "+1", "+5", "+3"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Ward"
    desc: "Every kami is bound to a ward: a specific animal, plant, object, or location. A kami can merge with or emerge from their ward as a single action, which has the concentrate trait. While merged, the kami can observe their surroundings with their usual senses as well as the senses of their ward, but can't move, communicate with, or control their ward. Additionally, a kami merged with their ward recovers Hit Points each minute as if they spent an entire day resting. <br>  <br> A zuishin's ward is typically a gate, doorway or shrine."
  - name: "Holy Weaponry"
    desc: "Any weapon becomes a *striking [[Holy]]* weapon while the zuishin wields it. A zuishin creates arrows out of nothing as part of their attacks with any bow they wield."
armorclass:
  - name: AC
    desc: "30; **Fort** +19, **Ref** +23, **Will** +17"
health:
  - name: HP
    desc: "180; **Weaknesses** cold iron 10"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Holy Katana +23 (`pf2:1`) (deadly d8, holy, magical, two hand d10, versatile p), **Damage** 2d6+9 slashing"
  - name: "Ranged strike"
    desc: "Holy Composite Longbow +24 (`pf2:1`) (deadly d10, holy, magical, reload 0, volley 30, range 100 ft.), **Damage** 2d8+9 piercing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29, attack +21<br>**5th** [[Breath of Life]]<br>**4th** [[Translocate]]<br>**2nd** [[Cleanse Affliction]], [[Dispel Magic]], [[Share Life]], [[Sure Footing]]<br>**1st** [[Heal]], [[Heal]]"
abilities_bot:
  - name: "Healing Arrow"
    desc: "`pf2:2` The zuishin blesses an arrow with healing magic. They expend a [[Breath of Life]], [[Cleanse Affliction]], [[Heal]], or [[Sure Footing]] spell and make a composite longbow Strike against an ally. <br>  <br> A critical failure has no effect, but on any other result the ally is affected by the spell rather than taking damage from the Strike."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Zuishin are kami warriors and archers tasked with watching over important shrines, ancient gates, or sacred doorways. With sturdy armor and hallowed armaments, zuishin fight tirelessly to drive off unholy powers who wish to desecrate their wards. Of all kami, zuishin most frequently fight against oni, as the wards zuishin guard are often targeted by these vile fiends.

Zuishin tend to regard mortals with skepticism. To earn a zuishin's trust, a supplicant might offer items of natural significance, such as an urn of hallowed earth, a branch from an ancient tree, or an arrangement of local flowers.

Like all kami, a zuishin might come across as reserved or even indifferent to humans and their ilk; however, this impression stems only from a zuishin's wisdom and longevity, which makes mortal affairs seem relatively trivial. In the company of other kami, they're unerringly benevolent and readily offer aid to their fellows. For example, a zuishin whose ward lies nestled in an ancient forest might readily join forces with kodama in those trees to deter foes.

Kami are divine nature spirits from the lands of Tian Xia, far to the east of the Inner Sea region. They serve as guardians of natural objects and places they protect—their wards—and are ancient enemies of oni (Pathfinder Monster Core 252–255). Kami can merge with their wards, allowing them to surreptitiously watch anyone who treads upon their sacred grounds. Kami leave those who they deem harmless alone, but fight vigilantly to scare away anyone perceived as a threat.

```statblock
creature: "Zuishin"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
