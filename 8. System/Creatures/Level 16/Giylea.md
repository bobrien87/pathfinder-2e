---
type: creature
group: ["Archon", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giylea"
level: "16"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Archon"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+28; [[Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Diabolic, Draconic, Empyrean, Utopian (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +31, Athletics +30, Intimidation +29, Religion +28, Warfare Lore +29"
abilityMods: ["+6", "+9", "+6", "+5", "+6", "+3"]
abilities_top: []
armorclass:
  - name: AC
    desc: "41 all-around vision; **Fort** +26, **Ref** +31, **Will** +28"
health:
  - name: HP
    desc: "230; **Immunities** fear effects; **Weaknesses** unholy 15"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "All-Knowing Eyes"
    desc: "30 feet. <br>  <br> When a creature ends its turn in the giylea's aura, it must attempt a DC 34 [[Will]] save. If the creature fails, any Deception check it attempts until the end of its next turn has its result reduced by one degree of success. If a creature is currently disguised or in a shape other than its true form when it fails its save, it also becomes [[Stupefied 1]] until the end of its next turn."
  - name: "Archon's Protection"
    desc: "`pf2:r` **Trigger** An enemy damages the archon's ally and both are within 15 feet of the archon <br>  <br> **Effect** The ally gains resistance 20 to all damage against the triggering damage and the archon can make a Strike against the enemy."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Slam +30 (`pf2:1`) (holy, magical, unarmed), **Damage** 1d6 fire plus 3d12+14 bludgeoning"
  - name: "Ranged strike"
    desc: "Tongue of Flame +33 (`pf2:1`) (fire, holy, magical), **Damage** 7d6 fire"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 37, attack +29<br>**9th** [[Detonate Magic]]<br>**7th** [[Divine Decree]]<br>**6th** [[Truesight]] (Constant), [[Zealous Conviction]]<br>**5th** [[Divine Immolation]], [[Scouting Eye]], [[Truespeech]] (Constant)<br>**4th** [[Divine Wrath]]<br>**3rd** [[Ring of Truth]] (At Will), [[Ring of Truth]] (Constant)"
abilities_bot:
  - name: "Fiery Spokes"
    desc: "`pf2:2` The giylea spins furiously, emitting a rain of divine fire. All creatures in a @Template[emanation|distance:60] take @Damage[(12d6)[fire],(5d6)[spirit]|options:area-damage]{12d6 fire damage and 5d6 spirit damage} with a DC 37 [[Reflex]] save. The giylea can't use Fiery Spokes for 1d4 rounds."
  - name: "Focus Gaze"
    desc: "`pf2:1` The giylea fixes their gaze on a creature they can see within 30 feet. The target must immediately attempt a DC 37 [[Will]] save against the giylea's all-knowing eyes. If the creature is under any magical effect that disguises it or has altered its shape, the giylea attempts to counter that magical disguise effect (counteract +29, 8th rank). After attempting its save, the creature is then temporarily immune until the start of the giylea's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Giyleas are known as wheel archons, named for their appearance as a flying, armor-plated wheel of fire with eyes on each spoke. They often serve as advisors due to their ability to see through lies, and they have a legendary intolerance and single-mindedness in the pursuit of the punishment of evil.

Archons are guardians of Heaven and enemies of corruption. Before gods and their servants set foot in the celestial planes, archons already resided in Heaven, the original inhabitants of the realm. Upon meeting, the archons and divine angels quickly discovered they were of a kind, holding justice and righteousness in their hearts. An alliance was formed, and archons now serve as stalwart allies to all celestials and mortals they find worthy.

While the first archons coalesced from the immense seven-tiered mountain of Heaven, they choose willing and worthy Heaven-bound souls to join their ranks. These mortals hear and answer the call of a mysterious voice, manifesting in the Garden at the mountain's peak. There they swear to forever serve the cause of justice and transform into their new archon forms.

Though deeply concerned with defending mortal life and willing to sacrifice themselves in battle against fiends, archons often feel rote and inscrutable to others, and their forms can border on frightening and bizarre. For this reason, they often have issues with interacting with mortals, or with the free spirited azatas. Despite this, archons draw great strength from others, especially those who exemplify virtue.

Beyond their celestial allies, archons also maintain ancient ties with aeons. The inscrutable factions can still be seen working together to defend longforgotten secrets and enforce rules that predate mortal life. Archons explain these missions as necessary without further elaboration, leaving even their angelic allies frustrated with archons' obstinance.

```statblock
creature: "Giylea"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
