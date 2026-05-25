---
type: creature
group: ["Beast", "Centaur"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Centaur Herbalist"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: "Centaur"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]]"
languages: "Common, Elven, Fey"
skills:
  - name: Skills
    desc: "Athletics +11, Diplomacy +6, Medicine +7, Nature +7, Survival +7"
abilityMods: ["+3", "+2", "+1", "+0", "+3", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +8, **Ref** +9, **Will** +9"
health:
  - name: HP
    desc: "40"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Hoof +9 (`pf2:1`) (agile), **Damage** 1d10+4 bludgeoning"
  - name: "Ranged strike"
    desc: "Sling +8 (`pf2:1`) (propulsive, reload 1, range 50 ft.), **Damage** 1d6+1 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Load Sachet"
    desc: "`pf2:1` **Requirements** The centaur herbalist has at least one herbal sachet; <br>  <br> **Effect** The centaur herbalist Interacts to load an herbal sachet in her sling. The next ranged Strike she makes with her sling deals an additional 1d6 poison damage."
  - name: "Trample"
    desc: "`pf2:3` Medium or smaller, hoof, DC 18 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Many centaurs are skilled in the study of plants, especially those in the areas in which they roam. They can use such herbs to both heal and cause distress in those who attack them.

Centaurs are legendary hunters and trackers who resemble heavily muscled humans with the bodies of powerful horses from the waist down. They are typically nomadic and consider themselves the stewards of the surrounding landscapes. While stories of bloody clashes between centaurs and humanoid travelers are well known, centaurs are neither intrinsically bloodthirsty nor recklessly aggressive. Rather, they are proud and stubborn and do not take kindly to outsiders who seeks to plunder the natural resources of the areas in which their communities have lived, some of which have been home to centaurs for thousands of years. Against despoilers of nature who fail to heed their warnings, centaurs do not hesitate to use their finely honed hunting skills to inflict deadly wounds.

Centaurs train with weapons as well as their heavy hooves, and the thunder of centaurs charging across the plains is often mistaken for a stampede or even an earthquake. Despite the tight bonds they form with their kin, some centaurs establish close alliances with elves, fey, gnomes, and isolated human communities. Such allies often benefit by learning from the centaurs' extensive knowledge of herbalism and wilderness survival. While centaurs enjoying traveling, most find it difficult to cut ties with their families and leave their bands to seek adventure in the wider world.

Centaurs have incredible variation in their individual size and coloration. Their upper torsos share the same variation in skin tone as other humanoids of their region, but their lower bodies—like those of horses—can vary widely from parent to child. Most centaurs are at least 7 feet tall and weigh more than 2,000 pounds.

Centaurs live in groups of dozens of members, usually led by an individual who has carried out many noble deeds and earned a lifetime of respect from their comrades. The revered leader guides the habits of their entire group; a wise seer might encourage the clan to roam far from civilization to preserve some unspoiled terrain, while an aggressive warrior might foster skirmishes with nearby humanoid settlements and rival centaur groups.

```statblock
creature: "Centaur Herbalist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
