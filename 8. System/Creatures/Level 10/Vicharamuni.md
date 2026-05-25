---
type: creature
group: ["Beast", "Holy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Vicharamuni"
level: "10"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: "Holy"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Darkvision]]"
languages: "Common, Empyrean"
skills:
  - name: Skills
    desc: "Acrobatics +22, Athletics +21, Deception +18, Diplomacy +21, Stealth +20, Heaven Lore +21"
abilityMods: ["+5", "+6", "+5", "+3", "+5", "+4"]
abilities_top:
  - name: "Coils of Knowledge"
    desc: "The naga's grip is more spiritual than physical. A creature hit by a vicharamuni's tail must succeed at a DC 29 [[Will]] save or become [[Grabbed]] by the tail until they [[Escape]], the naga releases them with an Interact action, or the naga dies. <br>  <br> A captive takes a –4 status penalty to Escape, but can choose to attempt an Occultism or Religion check to Escape instead of the usual options without taking this penalty"
  - name: "Spiritual Venom"
    desc: "A vicharamuni can choose to negate any damage that its venom does to a creature. In addition, the naga can cast any of its divine spells on a creature that is affected by its venom, regardless of range or line of effect."
  - name: "Vicharamuni Venom"
    desc: "**Saving Throw** DC 29 [[Will]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 3d6 spirit (1 round) <br>  <br> **Stage 2** 3d6 spirit and [[Drained]] 1 (1 round)"
armorclass:
  - name: AC
    desc: "31; **Fort** +20, **Ref** +21, **Will** +22"
health:
  - name: HP
    desc: "175"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +22 (`pf2:1`) (finesse, holy, reach 10 ft.), **Damage** 3d10+8 piercing plus [[Vicharamuni Venom]]"
  - name: "Melee strike"
    desc: "Tail +22 (`pf2:1`) (agile, finesse, holy, reach 20 ft.), **Damage** 3d8+8 bludgeoning plus [[Coils Of Knowledge]]"
  - name: "Ranged strike"
    desc: "Spit +22 (`pf2:1`) (agile, holy, poison, range 30 ft.), **Damage**  plus [[Vicharamuni Venom]]"
spellcasting:
  - name: "Divine Spontaneous Spells"
    desc: "DC 29, attack +21<br>**5th** (4 slots) [[Breath of Life]], [[Divine Immolation]]<br>**4th** (4 slots) [[Fly]]<br>**3rd** (4 slots) [[Crisis of Faith]], [[Holy Light]], [[Lightning Bolt]], [[Mind Reading]]<br>**2nd** (4 slots) [[Calm]], [[Cleanse Affliction]], [[Dispel Magic]], [[Noise Blast]], [[See the Unseen]]<br>**1st** (4 slots) [[Daze]], [[Detect Magic]], [[Frostbite]], [[Heal]], [[Light]], [[Protection]], [[Read Aura]], [[Spirit Link]], [[Stabilize]], [[Telekinetic Hand]]"
abilities_bot:
  - name: "Greater Constrict"
    desc: "`pf2:1` @Damage[(3d8+5)[bludgeoning]], DC 29 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC. A creature that fails this save falls [[Unconscious]], and a creature that succeeds is then temporarily immune to falling unconscious from Greater Constrict for 1 minute."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Awakener nagas are benevolent and wise teachers of people and places. They seek to guide and nurture the world around them, sensing mortals or locales with potential supernatural significance. Once located, these nagas provide instruction and divine trials to forge their wards toward strength and to impart a deeper understanding of right and wrong. Though considered stern and intimidating taskmasters by their students, those taught by a vicharamuni often go on to become great heroes.

Awakener nagas are similarly attentive in guiding their young. Upon reaching adulthood, a naga is provided a final trial before being encouraged to depart the nest and seek out their own natural wonders or promising mortals. Sometimes generations of nagas might guard the same place or family line, passing the honor of such care from parent to child. In such cases, the parent nagas aim to have at least one of their children elect to stay behind and become the guardian of their ancestral ward, giving the parents peace of mind that the site they protect will continue to be guarded by their descendants.

Nagas are serpentine beings with magical powers and keen intellects. Physically, they resemble massive snakes, though they often wear jewelry and other ornaments that clearly separate them from their animal kin. Nagas use their innate magic and poisonous fangs to keep all but the most stalwart foes at bay. They keep their own counsel, viewing their cosmic role to be sacrosanct and beyond the understanding of outside scholars. Their unwillingness to explain themselves or entertain the suggestion of alliances has led to a long history of conflict with their neighbors, who read them as aloof, arrogant, or duplicitous.

Nagas often have a powerful sense of duty to their perceived role within the universe, even if this role leads them to violent or tragic ends. Many see them as harsh and stern due to their devotion, terrifying in their majesty yet possessed of an aura of transcendence.

```statblock
creature: "Vicharamuni"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
